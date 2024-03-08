import asyncio
from pathlib import Path
import shutil

import pytest

from hangar_sdk.core.blocks.aws_blocks import (
    AwsEC2Instance,
    AwsSecurityGroup,
    Egress,
    Ingress,
    AwsSubnet,
    DefaultAwsVpc
)
from hangar_sdk.core.terraform import ResourceGroup

basepath = ".hangar"

@pytest.fixture(scope="session", autouse=True)
def file_setup():
    # Will be executed before the first test

    yield None
    # Will be executed after the last test

    dothangar = Path(basepath)

    # delete dothangar path recursively
    print("Tearing down environment")
    # shutil.rmtree(dothangar)

def test_ec2_instance():
    group = ResourceGroup(name="hello", region="us-west-1")

    sg = AwsSecurityGroup(
        ingress=[
            Ingress(
                from_port=22,
                to_port=22,
                protocol="TCP",
                cidr_blocks=["0.0.0.0/0"],
            )
        ],
        egress=[
            Egress(
                from_port=22,
                to_port=22,
                protocol="TCP",
                cidr_blocks=["0.0.0.0/0"],
            )
        ],
        name="hangar-e2e",
        group=group,
    )

    default = DefaultAwsVpc(name="default", group=group, tags={})

    subnet = AwsSubnet(
        name="subnet-a",
        group=group,
        vpc=default,
        availability_zone="us-west-1a",
        cidr_block="172.31.32.0/20",
        tags={},
    )

    instance = AwsEc2Instance(
        security_groups=[sg],
        instance_type="t2.micro",
        name="test-instance",
        group=group,
        architecture="x86_64",
        tags={},
        subnet=subnet
    )

    group.resolve()

    resource = instance.get_instance_client()
    resource.wait_until_running()
    group.buffer.load()

    assert sg.security_group.get_state()["values"]["arn"] is not None
    assert instance.instance.get_state()["values"]["public_ip"] is not None

    group.buffer.destroy()

    assert instance.instance.get_state()["values"]["public_ip"] is None
    assert sg.security_group.get_state()["values"]["arn"] is None
