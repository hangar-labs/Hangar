import hashlib
import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Sequence, TypedDict, Union

import boto3
from attr import Factory, define, field

from hangar_sdk.core import ExecutionType, IResource
from hangar_sdk.core.terraform import Resource, ResourceGroup
from hangar_sdk.resources.terraform import Expression
from hangar_sdk.resources.terraform.aws import (
    aws_alb,
    aws_autoscaling_group,
    aws_ebs_volume,
    aws_ecs_capacity_provider,
    aws_ecs_cluster,
    aws_ecs_cluster_capacity_providers,
    aws_ecs_service,
    aws_ecs_task_definition,
    aws_iam_instance_profile,
    aws_instance,
    aws_internet_gateway,
    aws_lambda_function,
    aws_lambda_layer_version,
    aws_lb_listener,
    aws_lb_target_group,
    aws_s3_bucket,
    aws_security_group,
    aws_subnet,
    aws_vpc,
    data_aws_ami,
    data_aws_vpc,
    aws_iam_policy,
    aws_iam_policy_attachment,
    aws_iam_role,
    aws_efs_file_system,
    aws_efs_mount_target
)
from hangar_sdk.resources.terraform.aws import aws_launch_template
from hangar_sdk.resources.terraform.aws.aws_launch_template import AwsLaunchTemplate
from hangar_sdk.core.rbac.aws.statement import Statement

# Bucket

# The Done Line ----------------

# VPC
# Subnet
# Volume
# IGW
# Loadbalancer (LB, Target group, Listener, need listener rules)
# Security Group

# Code Written -----------------

# ECS

# Lift and shift

# Instance
# Autoscale
# Lambda

# Docker compose to task defn
# Fargate


def hash_path(path):
    """Return a hash for the specified file or directory."""
    hasher = hashlib.sha1()
    if os.path.isfile(path):
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                filepath = os.path.join(root, name)
                hasher.update(hash_path(filepath).encode())
    return hasher.hexdigest()


@define(kw_only=True, slots=False)
class AwsIamRole(Resource):
    name: str
    group: "ResourceGroup"
    _dependencies: list = field(default=Factory(list))
    assume_role_policy: Optional[dict] = None
    inline_policy: Optional[dict] = None
    managed_policy_arns: Optional[Sequence[str]] = None
    
    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:

        self.role = aws_iam_role.AwsIamRole(
            top_name=self.name,
            group=self.group,
            name=self.name,
            assume_role_policy=json.dumps(json.dumps(self.assume_role_policy))[1:-1] if self.assume_role_policy else None,
            inline_policy=json.dumps(json.dumps(self.inline_policy))[1:-1] if self.inline_policy else None,
            managed_policy_arns=self.managed_policy_arns if self.managed_policy_arns else None
        )

        return [self.role]


@define(kw_only=True, slots=False)
class AwsBucket(Resource):
    name: str
    group: "ResourceGroup"
    _dependencies: list = field(default=Factory(list))
    tags: Optional[dict] = None

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.bucket = aws_s3_bucket.AwsS3Bucket(
            group=self.group,
            top_name=self.name,
            bucket=self.name,
            tags=self.tags,
            force_destroy=True,
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        return [self.bucket]

    def allows(self, policy):
        s = Statement(policy=policy).aws_s3(resources=[self.bucket])
        policy.allows(s)
        return s


    def get_client(self):
        return boto3.client("s3")

    def put_object(self, key: str, source: str):
        print(f"Uploading Object to bucket {self.name}")

        client = self.get_client()
        client.upload_file(source, self.name, key)

        print(f"Finished Uploading Object to bucket {self.name}")


@define(kw_only=True, slots=False)
class DefaultAwsVpc(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    tags: Optional[dict]

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.vpc = data_aws_vpc.DataAwsVpc(
            top_name=self.name,
            group=self.group,
            default=True,
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        
        return [self.vpc]


@define(kw_only=True, slots=False)
class AwsVpc(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    cidr_block: str
    tags: dict

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.vpc = aws_vpc.AwsVpc(
            group=self.group,
            top_name=self.name,
            cidr_block=self.cidr_block,
            tags=self.tags,
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:

        return [self.vpc]


@define(kw_only=True, slots=False)
class AwsSubnet(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    vpc: Union[AwsVpc, DefaultAwsVpc]
    cidr_block: Optional[str] = None
    availability_zone: str
    tags: dict
    public: bool = True

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        self.subnet = aws_subnet.AwsSubnet(
            group=self.group,
            top_name=self.name,
            cidr_block=self.cidr_block if self.cidr_block else "0.0.0.0/0",
            availability_zone=self.availability_zone,
            tags=self.tags,
            map_public_ip_on_launch=self.public,
            vpc_id=self.vpc.vpc.ref().id,
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        return [self.subnet]


@define(kw_only=True, slots=False)
class AwsVolume(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    availability_zone: str
    size: int
    tags: Optional[dict]

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.volume = aws_ebs_volume.AwsEbsVolume(
            group=self.group,
            top_name=self.name,
            availability_zone=self.availability_zone,
            size=self.size,
            tags=self.tags if self.tags else None,
        )

        return [self.volume]


@define(kw_only=True, slots=False)
class AwsInternetGateway(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    tags: Optional[Dict[str, str]] = None
    tags_all: Union[Dict[str, str], None] = None
    vpc: AwsVpc

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.ig = aws_internet_gateway.AwsInternetGateway(
            top_name=self.name,
            group=self.group,
            tags=self.tags,
            tags_all=self.tags_all,
            vpc_id=self.vpc.vpc.ref().id,
        )

        return [self.ig]


@define(kw_only=True, slots=False)
class Ingress:
    to_port: int
    from_port: int
    protocol: str
    cidr_blocks: Optional[List[str]] = None


@define(kw_only=True, slots=False)
class Egress:
    to_port: int
    from_port: int
    protocol: str
    cidr_blocks: Optional[List[str]] = None


@define(kw_only=True, slots=False)
class AwsSecurityGroup(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    egress: Optional[List[Egress]] = None
    ingress: Optional[List[Ingress]] = None

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.security_group = aws_security_group.AwsSecurityGroup(
            top_name=self.name,
            group=self.group,
            description=None,
            egress=[
                aws_security_group.Egress(
                    group=self.group,
                    from_port=egress.from_port,
                    to_port=egress.to_port,
                    protocol=egress.protocol,
                    cidr_blocks=egress.cidr_blocks,
                )
                for egress in self.egress
            ]
            if self.egress
            else None,
            ingress=[
                aws_security_group.Ingress(
                    group=self.group,
                    from_port=ingress.from_port,
                    to_port=ingress.to_port,
                    protocol=ingress.protocol,
                    cidr_blocks=ingress.cidr_blocks,
                )
                for ingress in self.ingress
            ]
            if self.ingress
            else None,
            name=self.name,
            name_prefix=None,
            revoke_rules_on_delete=None,
            tags=None,
            tags_all=None,
            timeouts=None,
            vpc_id=None,
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:

        return [self.security_group]


@define(kw_only=True, slots=False)
class AwsLoadBalancer(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    tags: Optional[Dict[str, str]] = None
    internal: bool = False
    securityGroups: List[AwsSecurityGroup]
    subnets: List[AwsSubnet]

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.lb = aws_alb.AwsAlb(
            top_name=self.name,
            group=self.group,
            internal=self.internal,
            security_groups=[sg.security_group.ref().id for sg in self.securityGroups]
            if self.securityGroups
            else None,
            subnets=[subnet.subnet.ref().id for subnet in self.subnets]
            if self.subnets
            else None,
            tags=self.tags,
        )

        return [self.lb]


@define(kw_only=True, slots=False)
class AwsLbTargetGroup(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    port: int
    protocol: str
    healthcheck_path: str
    vpc_id: str

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.target_group = aws_lb_target_group.AwsLbTargetGroup(
            group=self.group,
            top_name=self.name,
            name=self.name,
            port=self.port,
            protocol=self.protocol,
            vpc_id=self.vpc_id,
            health_check=[
                aws_lb_target_group.HealthCheck(
                    group=self.group, path=self.healthcheck_path
                )
            ],
        )

        return [self.target_group]


@define(kw_only=True, slots=False)
class AwsLbListener(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    load_balancer: AwsLoadBalancer
    port: int
    protocol: str
    target_group: AwsLbTargetGroup

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.aws_lb_listener = aws_lb_listener.AwsLbListener(
            top_name=self.name,
            group=self.group,
            load_balancer_arn=self.load_balancer.lb.ref().arn,
            port=self.port,
            protocol=self.protocol,
            default_action=[
                aws_lb_listener.DefaultAction(
                    group=self.group,
                    type="forward",
                    target_group_arn=self.target_group.target_group.ref().arn,
                )
            ],
        )

        return [self.aws_lb_listener]


@define(kw_only=True, slots=False)
class AwsEc2Instance(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    ami: Optional[str] = None
    instance_type: str
    architecture: Union[Literal["x86_64"], Literal["arm64"]]
    subnet: AwsSubnet
    tags: dict
    os: str = "ubuntu"
    security_groups: List[AwsSecurityGroup] = field(default=Factory(list)),
    launch_script: str = None

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.ubuntu2204 = data_aws_ami.DataAwsAmi(
            top_name=self.name + "-ami",
            group=self.group,
            most_recent=True,
            owners=["099720109477"],
            filter=[
                data_aws_ami.Filter(
                    group=self.group,
                    name="architecture",
                    values=[self.architecture],
                ),
                data_aws_ami.Filter(
                    group=self.group,
                    name="virtualization-type",
                    values=["hvm"],
                ),
                data_aws_ami.Filter(
                    group=self.group,
                    name="name",
                    values=[
                        "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-*"
                        if self.architecture == "x86_64"
                        else "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-arm64-*"
                    ],
                ),
            ],
        )

        self.instance = aws_instance.AwsInstance(
            group=self.group,
            top_name=self.name,
            ami=self.ami if self.ami else self.ubuntu2204.ref().id,
            instance_type=self.instance_type,
            subnet_id=self.subnet.subnet.ref().id,
            tags=self.tags,
            vpc_security_group_ids=[sg.security_group.ref().id for sg in self.security_groups],
            user_data=Expression(
                f'base64encode({json.dumps(self.launch_script)})'
            ) if self.launch_script is not None else None
        )

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:

        return [self.ubuntu2204, self.instance]

    def get_instance_client(self):
        return boto3.resource("ec2")

    def run_commands(self, commands: List[str]):
        pass


@define(kw_only=True, slots=False)
class ArchiveAsset(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    path: str
    bucket: AwsBucket

    @property
    def computed_path(self):
        return os.path.basename(self.path) + "-" + hash_path(self.path)

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        if type == "create":
            print(f"Syncing asset archive {self.name}")

            self.bucket.put_object(
                key=self.computed_path,
                source=self.path,
            )

            print(f"Finished syncing asset archive {self.name}")

        return []


@define(kw_only=True, slots=False)
class LambdaLayer(Resource):
    asset: ArchiveAsset
    group: ResourceGroup
    runtimes: Union[List[str], None] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.layer = aws_lambda_layer_version.AwsLambdaLayerVersion(
            group=self.group,
            top_name=self.name,
            s3_bucket=self.asset.bucket.bucket.ref().id,
            s3_key=os.path.basename(self.asset.computed_path),
            compatible_runtimes=self.runtimes,
            layer_name=self.name,
        )

        return [self.layer]

    def get_client(self):
        return boto3.client("lambda")


@define(kw_only=True, slots=False)
class LambdaFunction(Resource):
    name: str
    function_name: str
    group: ResourceGroup
    asset: ArchiveAsset
    runtime: str
    handler: str
    role: str
    timeout: Optional[int] = None
    environment: Union[Dict[str, str], None] = None
    layers: Union[List[LambdaLayer], None] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:

        self.function = aws_lambda_function.AwsLambdaFunction(
            group=self.group,
            top_name=self.name,
            function_name=self.function_name,
            s3_bucket=self.asset.bucket.bucket.ref().id,
            s3_key=os.path.basename(self.asset.computed_path),
            runtime=self.runtime,
            handler=self.handler,
            timeout=self.timeout,
            role=self.role,
            environment=[
                aws_lambda_function.Environment(
                    group=self.group, variables=self.environment
                )
            ],
            layers=[layer.layer.ref().arn for layer in self.layers]
            if self.layers
            else None,
        )

        return [self.function]

    def get_client(self):
        return boto3.client("lambda")

    def invoke(self, payload: dict):
        client = self.get_client()
        response = client.invoke(
            FunctionName=self.state["aws_lambda_function"][self.name]["values"][
                "function_name"
            ],
            Payload=json.dumps(payload),
        )
        return json.loads(response["Payload"].read().decode("utf-8"))


@define(kw_only=True, slots=False)
class AwsInstanceLaunchTemplate(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    ami: Optional[str] = None
    instance_type: str
    architecture: Union[Literal["x86_64"], Literal["arm64"]]
    security_groups: List[AwsSecurityGroup] = field(default=Factory(list)),
    launch_script: Optional[str] = None,
    version: Optional[str] = None
    key_pair_name: str = None,
    instance_role: AwsIamRole

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.profile = aws_iam_instance_profile.AwsIamInstanceProfile(
            group=self.group,
            top_name=self.name + "_instance_profile",
            name_prefix=self.name,
            role=self.instance_role.role.ref().name,
        )

        self.lt = aws_launch_template.AwsLaunchTemplate(
            group=self.group,
            top_name=self.name,
            image_id=self.ami,
            instance_type=self.instance_type,
            iam_instance_profile=[aws_launch_template.IamInstanceProfile(
                group=self.group,
                name=self.profile.ref().name
            )],
            vpc_security_group_ids=[sg.security_group.ref().id for sg in self.security_groups],
            user_data=Expression(
                f'base64encode({json.dumps(self.launch_script)})'
            ) if self.launch_script is not None else None,
            name=self.name,
            key_name=self.key_pair_name,
        )

        return [self.profile, self.lt]

    @classmethod
    def from_instance(cls, instance: AwsEc2Instance):
        return cls(
            name=instance.name + "_launch_template",
            group=instance.group,
            version="$Latest",
            image_id=instance.instance.ref().ami,
            instance_type=instance.instance_type,
            key_name=instance.instance.ref().key_name,
            user_data=instance.instance.ref().user_data,
        )


@define(kw_only=True, slots=False)
class InstanceAutoScaler(Resource):
    vpc: AwsVpc
    subnets: List[AwsSubnet]
    minSize: int
    maxSize: int
    desiredCapacity: int
    launchTemplate: AwsInstanceLaunchTemplate
    targetGroups: Optional[List[AwsLbTargetGroup]]

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.asg = aws_autoscaling_group.AwsAutoscalingGroup(
            top_name=self.name,
            group=self.group,
            vpc_zone_identifier=[
                subnet.subnet.ref().id for subnet in self.subnets
            ],
            desired_capacity=self.desiredCapacity,
            max_size=self.maxSize,
            min_size=self.minSize,
            launch_template=[
                aws_autoscaling_group.LaunchTemplate(
                    group=self.group,   
                    name=self.launchTemplate.lt.ref().name,
                    version=self.launchTemplate.lt.ref().latest_version,
                )
            ],
            target_group_arns=[tg.target_group.ref().arn for tg in self.targetGroups] if self.targetGroups else None,
        )

        return [self.asg]

    def from_instance(cls, instance: AwsEc2Instance):
        return cls(
            vpc=instance.vpc,
            subnets=instance.subnets,
            minSize=1,
            maxSize=1,
            desiredCapacity=1,
            launchTemplate=AwsInstanceLaunchTemplate.from_instance(instance),
            targetGroupArns=[],
        )
    

@define(kw_only=True, slots=False)
class AwsEcsCapacityProvider(Resource):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    managed_scaling: Optional[Dict[str, Any]] = None
    autoscale_group: Optional[InstanceAutoScaler] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.capacity_provider = aws_ecs_capacity_provider.AwsEcsCapacityProvider(
            group=self.group,
            top_name=self.name,
            name=self.name,
            auto_scaling_group_provider=aws_ecs_capacity_provider.AutoScalingGroupProvider(
                group=self.group,
                managed_scaling=self.managed_scaling,
                auto_scaling_group_arn=self.autoscale_group.asg.ref().arn,
            ) 
        )

        return [self.capacity_provider]

@define(kw_only=True, slots=False)
class AwsEcsCluster(Resource):
    name: str
    group: ResourceGroup
    capacity_providers: Optional[List[AwsEcsCapacityProvider]] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.cluster = aws_ecs_cluster.AwsEcsCluster(
            group=self.group,
            top_name=self.name,
            name=self.name,
            configuration=[
                aws_ecs_cluster.Configuration(
                    group = self.group,
                    execute_command_configuration=[aws_ecs_cluster.ExecuteCommandConfiguration(
                        group=self.group,
                        logging="DEFAULT",
                    )]
                )
            ],
            setting=[aws_ecs_cluster.Setting(
                group=self.group,
                name="containerInsights",
                value="enabled"
            )],
        )

        self.capacity_providers = aws_ecs_cluster_capacity_providers.AwsEcsClusterCapacityProviders(
            top_name=self.name + "_capacity_providers",
            group=self.group,
            cluster_name=self.name,
            capacity_providers=[cp.name for cp in self.capacity_providers],
            default_capacity_provider_strategy=[
                aws_ecs_cluster_capacity_providers.DefaultCapacityProviderStrategy(
                    group=self.group,
                    base=1,
                    # equal 
                    weight=100,
                    capacity_provider=self.capacity_providers[0].name,
                )
            ] if self.capacity_providers else None,
        )

        return [self.cluster, self.capacity_providers]

    def get_client(self):
        return boto3.client("ecs")


class PortMapping(TypedDict):
    containerPort: int
    appProtocol: Optional[Union[Literal["HTTP"], Literal["HTTP2"], Literal["GRPC"]]] = None
    hostPort: Optional[int] = None

class CredentialsParameter(TypedDict):
    credentialsParameter: str

class HealthCheck(TypedDict):
    command: List[str]
    interval: int
    retries: int
    startPeriod: int
    timeout: int

class EnvironmentFile(TypedDict):
    value: str 
    type: str = "s3"

class EnvironmentEntry(TypedDict):
    name: str
    value: str

class LogConfiguration(TypedDict):
    name: str
    valueFrom: str

class MountPoint(TypedDict):
    containerPath: str
    readOnly: Optional[bool]
    sourceVolume: str
    volumesFrom: Optional[List[Dict[str, str]]]

class SecretOptions(TypedDict):
    name: str
    valueFrom: str

class FirelensConfiguration(TypedDict):
    type: str
    options: Dict[str, str]
    type: Union[Literal["fluentbit"], Literal["fluentd"]]

class LogConfiguration(TypedDict):
    logDriver: Union[Literal["awslogs"], Literal["fluentd"], Literal["gelf"], Literal["json-file"], Literal["journald"], Literal["logentries"], Literal["splunk"], Literal["syslog"], Literal["awsfirelens"]]
    options: Dict[str, str]
    secretOptions: Optional[List[SecretOptions]]
    firelensConfiguration: Optional[FirelensConfiguration]

class ContainerDependency(TypedDict):
    condition: str
    containerName: str  

class ContainerDefinition(TypedDict):
    name: str
    image: str
    cpu: int
    memory: Optional[int]
    memory_reservation: Optional[int]
    portMappings: Optional[List[PortMapping]] = None
    repositoryCredentials: Optional[CredentialsParameter] = None
    healthcheck: Optional[HealthCheck] = None
    environment: Optional[Dict[str, str]] = None
    disableNetworking: bool
    links : Optional[List[str]]
    hostname: Optional[str]
    dnsServers: Optional[List[str]]
    dnsSearchDomains: Optional[List[str]]
    extraHosts: Optional[List[Dict[str, str]]]
    gpu: Optional[int]
    essential: bool
    entryPoint: Optional[List[str]]
    command: Optional[List[str]]
    workingDirectory: Optional[str]
    environmemntFiles: Optional[List[EnvironmentFile]]
    environment: Optional[List[EnvironmentEntry]]
    secrets: Optional[List[str]]
    readonlyRootFilesystem: Optional[bool]
    mountPoints: Optional[List[MountPoint]]
    LogConfiguration: Optional[LogConfiguration]
    privileged: Optional[bool]
    user : Optional[str]
    dockerSecurityOptions: Optional[List[str]]
    ulimits: Optional[List[Dict[str, str]]]
    dockerLabels: Optional[Dict[str, str]]
    linuxParameters: Optional[Dict[str, str]]
    dependsOn:  Optional[List[ContainerDependency]]
    startTimeout: Optional[int]
    stopTimeout: Optional[int]
    systemControls: Optional[List[Dict[str, str]]]
    interactive: Optional[bool]
    pseudoTerminal: Optional[bool]

class DockerVolumeConfiguration(TypedDict):
    scope: str
    autoprovision: bool
    driver: str
    driverOpts: Dict[str, str]
    labels: Dict[str, str]

class VolumeDefinition(TypedDict):
    name: str
    host: Optional[Dict[str, str]]
    sourcePath: Optional[str]
    configuredAtLaunch: Optional[bool]
    dockerVolumeConfiguration: Optional[Dict[str, str]]
    efsVolumeConfiguration: Optional[Dict[str, str]]

@define(kw_only=True, slots=False)
class AwsElasticFileSystem(Resource):
    name: str
    group: ResourceGroup
    availability_zone_name: str
    subnet: AwsSubnet

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        
        self.fs = aws_efs_file_system.AwsEfsFileSystem(
            top_name=self.name,
            group=self.group,
            creation_token = self.name + "_creation_token",
            availability_zone_name=self.availability_zone_name
        )

        self.mt = aws_efs_mount_target.AwsEfsMountTarget(
            top_name=self.name + "_mount_target",
            group=self.group,
            file_system_id=self.fs.ref().id,
            subnet_id=self.subnet.subnet.ref().id
        )

        return [self.fs, self.mt]

@define(kw_only=True, slots=False)
class AwsEcsTaskDefinition(Resource):
    family: str
    requires_compatibilities: List[Union[Literal["FARGATE"], Literal["EC2"], Literal["EXTERNAL"]]]
    task_role : AwsIamRole
    execution_role: AwsIamRole
    network_mode: Union[Literal["awsvpc"], Literal["bridge"], Literal["host"]]
    cpu_architecture: Union[Literal["X86_64"], Literal["ARM64"]] = "X86_64"
    cpu : Union[Literal["256"], Literal["512"], Literal["1024"], Literal["2048"], Literal["4096"], Literal["8192"], Literal["16384"]] = "1024"
    memory: str = "2048"
    container_definitions: List[ContainerDefinition]
    volumes: Optional[Sequence[AwsElasticFileSystem]] = None
    tags: Optional[Dict[str, str]] = None
    emphemeral_storage_size: Optional[int] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.task_definition = aws_ecs_task_definition.AwsEcsTaskDefinition(
            top_name=self.name,
            group=self.group,
            container_definitions=json.dumps(json.dumps(self.container_definitions))[1:-1],
            family=self.family,
            cpu=self.cpu,
            ephemeral_storage=[aws_ecs_task_definition.EphemeralStorage(group=self.group, size_in_gib=self.emphemeral_storage_size)] if self.emphemeral_storage_size else None,
            execution_role_arn=self.execution_role.role.ref().arn,
            memory=self.memory,
            network_mode=self.network_mode,
            requires_compatibilities=self.requires_compatibilities,
            runtime_platform=aws_ecs_task_definition.RuntimePlatform(group=self.group, cpu_architecture=self.cpu_architecture),
            task_role_arn=self.task_role.role.ref().arn,
            volume=[
                aws_ecs_task_definition.Volume(
                    group=self.group,
                    name=volume.name,
                    efs_volume_configuration=aws_ecs_task_definition.EfsVolumeConfiguration(
                        group=self.group,
                        file_system_id=volume.fs.ref().id
                    )
                ) for volume in self.volumes
            ] if self.volumes else None
        )  

        return [self.task_definition]
    
    # check that if fargate then network mode is awsvpc
    # if fargate memory = Amount (in MiB) of memory used by the task 

@define(kw_only=True, slots=False)
class AwsEcsService(Resource):
    name: str
    group: ResourceGroup
    cluster: AwsEcsCluster
    task_definition: AwsEcsTaskDefinition
    container_name: str
    container_port: int
    # launch_type: strx
    desired_count: int
    force_new_deployment: bool = True
    capacity_provider: AwsEcsCapacityProvider
    target_group: AwsLbTargetGroup
    order_strategy: Optional[Union[Literal['binpack'], Literal['random'], Literal['spread']]] = None

    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        self.service = aws_ecs_service.AwsEcsService(
            group=self.group,
            top_name=self.name,
            name=self.name,
            cluster=self.cluster.cluster.name,
            task_definition=self.task_definition.task_definition.ref().arn,
            desired_count=self.desired_count,
            force_new_deployment=self.force_new_deployment,
            ordered_placement_strategy=aws_ecs_service.OrderedPlacementStrategy(
                group=self.group,
                type=self.order_strategy,
                field="cpu" if self.order_strategy == "binpack" else None,
            ),
            deployment_circuit_breaker=aws_ecs_service.DeploymentCircuitBreaker(
                group=self.group,
                enable=True,
                rollback=True,
            ),
            load_balancer=[
                aws_ecs_service.LoadBalancer(
                    group=self.group,
                    target_group_arn=self.target_group.target_group.ref().arn,
                    container_name=self.container_name,
                    container_port=self.container_port,
                )
            ],
            capacity_provider_strategy=[
                aws_ecs_service.CapacityProviderStrategy(
                    group=self.group,
                    capacity_provider=self.capacity_provider.capacity_provider.ref().name,
                    weight=100
                )
            ]
        )

        return [self.service]

    def get_client(self):
        return boto3.client("ecs")
