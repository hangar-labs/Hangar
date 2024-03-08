import asyncio
import json
from pathlib import Path
import shutil
from hangar_sdk.resources.terraform.aws import data_aws_ami

import pytest

from hangar_sdk.core.blocks.aws_blocks import (
    AwsSecurityGroup,
    AwsVolume,
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

    task_role = AwsIamRole(
        name="test-ecs-role",
        group=group,
        managed_policy_arns=["arn:aws:iam::aws:policy/AdministratorAccess", "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"],
        assume_role_policy={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {"Service": ["ecs.amazonaws.com", "ecs-tasks.amazonaws.com", "ecs.application-autoscaling.amazonaws.com", "ec2.amazonaws.com"]},
                    "Effect": "Allow",
                }
            ],
        }
    )

    sg = AwsSecurityGroup(
        ingress=[
            Ingress(
                from_port=0,
                to_port=0,
                protocol="-1",
                cidr_blocks=["0.0.0.0/0"],
            ),
        ],
        egress=[
            Egress(
                from_port=0,
                to_port=0,
                protocol="-1",
                cidr_blocks=["0.0.0.0/0"],
            ),
        ],
        name="hangar-e2e",
        group=group,
    )

    default = DefaultAwsVpc(name="default", group=group, tags={})

    az = "us-west-1a"

    subnet = AwsSubnet(
        name="subnet-a",
        group=group,
        vpc=default,
        availability_zone=az,
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

    ecs_ami = data_aws_ami.DataAwsAmi(
        top_name="ecs_ami",
        group=group,
        filter=[
            data_aws_ami.Filter(
                name="name",
                group=group,
                values=["amzn2-ami-ecs-hvm-2.0.20231103-x86_64-ebs"],
            ),
            data_aws_ami.Filter(
                group=group,
                name="architecture",
                values=["x86_64"],
            ),
        ],
    )

    group.buffer.add(ecs_ami)

    cluster_name = "test_cluster"

    volume = AwsVolume(
        name="test_volume",
        group=group,
        availibilty_zone=az,
        size=200
    )

    launch_template = AwsInstanceLaunchTemplate(
        security_groups=[sg],
        ami=ecs_ami.ref().id,
        instance_type="t2.micro",
        name="test-instance",
        group=group,
        architecture="X86_64",
        launch_script=f"#!/bin/bash\necho ECS_CLUSTER={cluster_name} >> /etc/ecs/ecs.config",
        key_pair_name="wooooo",
        instance_role=task_role
    )

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

    lb_listener = AwsLbListener(
        name="listener",
        group=group,
        load_balancer=lb,
        port=80,
        protocol="HTTP",
        target_group=target_group
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
        name=cluster_name,
        group=group,
        capacity_providers=[capacity_provider]
    )

    cd = ContainerDefinition(
        name="some_container",
        image="public.ecr.aws/nginx/nginx:stable",
        cpu=512,
        memory=512,
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
            )
        ]
    )

    task = AwsEcsTaskDefinition(
        name="task",
        group=group,
        family="aloha",
        requires_compatibilities=["EC2"],
        task_role=task_role,
        execution_role=task_role,
        network_mode="bridge",
        cpu="512",
        memory="512",
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

