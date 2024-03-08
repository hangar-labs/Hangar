import asyncio
import json
from pathlib import Path
import shutil

import pytest

from hangar_sdk.core.blocks.aws_blocks import (
    AwsSecurityGroup,
    Egress,
    Ingress,
    AwsSubnet,
    DefaultAwsVpc,
    AwsEc2Instance,
    AwsEcsService,
    AwsEcsTaskDefinition,
    AwsEcsCluster,
    AwsEcsCapacityProvider,
    InstanceAutoScaler,
    AwsLoadBalancer,
    AwsLbTargetGroup,
    AwsLbListener,
    AwsInstanceLaunchTemplate,
    ContainerDefinition,
    PortMapping,
    AwsIamRole
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
    group = ResourceGroup(name="hello", region="us-west-1", terraform_excecutable="/opt/homebrew/bin/terraform")

    sg = AwsSecurityGroup(
        ingress=[
            Ingress(
                from_port=22,
                to_port=22,
                protocol="TCP",
                cidr_blocks=["0.0.0.0/0"],
            ),
            Ingress(
                from_port=80,
                to_port=80,
                protocol="TCP",
                cidr_blocks=["0.0.0.0/0"],
            ),
            Ingress(
                from_port=443,
                to_port=443,
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
            ),
            Egress(
                from_port=80,
                to_port=80,
                protocol="TCP",
                cidr_blocks=["0.0.0.0/0"],
            ),
            Egress(
                from_port=443,
                to_port=443,
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

    subnet2 = AwsSubnet(
        name="subnet-b",
        group=group,
        vpc=default,
        availability_zone="us-west-1b",
        cidr_block="172.31.64.0/20",
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

    launch_template = AwsInstanceLaunchTemplate.from_instance(instance)

    target_group = AwsLbTargetGroup(
        name="test-targetgroup",
        group=group,
        port=80,
        protocol="HTTP",
        healthcheck_path="/",
        vpc_id=default.vpc.ref().id
    )

    lb = AwsLoadBalancer(
        name="loadBalancer",
        group=group,
        securityGroups=[sg],
        subnets=[subnet, subnet2]
    )

    autoscaler = InstanceAutoScaler(
        name="instance_auto_scaler",
        group=group,
        vpc=default,
        subnets=[subnet],
        minSize=0,
        maxSize=2,
        desiredCapacity=1,
        launchTemplate=launch_template,
        targetGroups=[target_group]
    )

    capacity_provider = AwsEcsCapacityProvider(
        name="capacity_provider",
        group=group,
        autoscale_group=autoscaler
    )

    cluster = AwsEcsCluster(
        name="test_cluster",
        group=group,
        capacity_providers=[capacity_provider]
    )

    cd = ContainerDefinition(
        name="some_container",
        image="public.ecr.aws/nginx/nginx:stable",
        cpu=512,
        portMappings=[
            PortMapping(
                containerPort=80,
                appProtocol="http",
                hostPort=80
            ),
            PortMapping(
                containerPort=443,
                appProtocol="http",
                hostPort=443
            ),
            PortMapping(
                containerPort=22,
                appProtocol="http",
                hostPort=22
            )
        ]
    )

    task_role = AwsIamRole(
        name="test-ecs-role",
        group=group,
        managed_policy_arns=["arn:aws:iam::aws:policy/AdministratorAccess"],
        assume_role_policy={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {"Service": "ecs.amazonaws.com"},
                    "Effect": "Allow",
                }
            ],
        }
    )

    task = AwsEcsTaskDefinition(
        name="task",
        group=group,
        family="aloha",
        requires_compatibilities=["EC2"],
        task_role=task_role,
        execution_role=task_role,
        network_mode="bridge",
        cpu="1024",
        memory="2048",
        container_definitions=[cd]
    )

    service = AwsEcsService(
        name="ecs_service",
        group=group,
        cluster=cluster,
        task_definition=task,
        container_name=cd["name"],
        container_port=80,
        desired_count=1,
        capacity_provider=capacity_provider,
        target_group=target_group,
        order_strategy="binpack"
    )

    group.resolve()

