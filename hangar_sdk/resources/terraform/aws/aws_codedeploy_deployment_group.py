from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AlarmConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="alarm_configuration")
    alarms: Optional[Sequence[str]] = None
    enabled: Optional[bool] = None
    ignore_poll_alarm_failure: Optional[bool] = None


@define(kw_only=True, slots=False)
class AutoRollbackConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="auto_rollback_configuration")
    enabled: Optional[bool] = None
    events: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class DeploymentReadyOption(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="deployment_ready_option")
    action_on_timeout: Optional[str] = None
    wait_time_in_minutes: Optional[int] = None


@define(kw_only=True, slots=False)
class GreenFleetProvisioningOption(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="green_fleet_provisioning_option")
    action: Optional[str] = None


@define(kw_only=True, slots=False)
class TerminateBlueInstancesOnDeploymentSuccess(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(
        alias="_name", default="terminate_blue_instances_on_deployment_success"
    )
    action: Optional[str] = None
    termination_wait_time_in_minutes: Optional[int] = None


@define(kw_only=True, slots=False)
class BlueGreenDeploymentConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="blue_green_deployment_config")
    deployment_ready_option: Optional[Sequence[DeploymentReadyOption]] = None
    green_fleet_provisioning_option: Optional[
        Sequence[GreenFleetProvisioningOption]
    ] = None
    terminate_blue_instances_on_deployment_success: Optional[
        Sequence[TerminateBlueInstancesOnDeploymentSuccess]
    ] = None


@define(kw_only=True, slots=False)
class DeploymentStyle(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="deployment_style")
    deployment_option: Optional[str] = None
    deployment_type: Optional[str] = None


@define(kw_only=True, slots=False)
class Ec2TagFilter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ec2_tag_filter")
    key: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class Ec2TagFilter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ec2_tag_filter")
    key: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class Ec2TagSet(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ec2_tag_set")
    ec2_tag_filter: Optional[Sequence[Ec2TagFilter]] = None


@define(kw_only=True, slots=False)
class EcsService(AbstractTerraformBlock):
    cluster_name: str
    service_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ecs_service")


@define(kw_only=True, slots=False)
class ElbInfo(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="elb_info")
    name: Optional[str] = None


@define(kw_only=True, slots=False)
class TargetGroupInfo(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_group_info")
    name: Optional[str] = None


@define(kw_only=True, slots=False)
class ProdTrafficRoute(AbstractTerraformBlock):
    listener_arns: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="prod_traffic_route")


@define(kw_only=True, slots=False)
class TargetGroup(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_group")


@define(kw_only=True, slots=False)
class TestTrafficRoute(AbstractTerraformBlock):
    listener_arns: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="test_traffic_route")


@define(kw_only=True, slots=False)
class TargetGroupPairInfo(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_group_pair_info")
    prod_traffic_route: Optional[Sequence[ProdTrafficRoute]] = None
    target_group: Optional[Sequence[TargetGroup]] = None
    test_traffic_route: Optional[Sequence[TestTrafficRoute]] = None


@define(kw_only=True, slots=False)
class LoadBalancerInfo(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="load_balancer_info")
    elb_info: Optional[Sequence[ElbInfo]] = None
    target_group_info: Optional[Sequence[TargetGroupInfo]] = None
    target_group_pair_info: Optional[Sequence[TargetGroupPairInfo]] = None


@define(kw_only=True, slots=False)
class OnPremisesInstanceTagFilter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="on_premises_instance_tag_filter")
    key: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class TriggerConfiguration(AbstractTerraformBlock):
    trigger_events: Sequence[str]
    trigger_name: str
    trigger_target_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="trigger_configuration")


@define(kw_only=True, slots=False)
class AwsCodedeployDeploymentGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    app_name: str
    deployment_group_name: str
    service_role_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codedeploy_deployment_group")
    alarm_configuration: Optional[Sequence[AlarmConfiguration]] = None
    auto_rollback_configuration: Optional[Sequence[AutoRollbackConfiguration]] = None
    autoscaling_groups: Optional[Sequence[str]] = None
    blue_green_deployment_config: Optional[Sequence[BlueGreenDeploymentConfig]] = None
    deployment_config_name: Optional[str] = None
    deployment_style: Optional[Sequence[DeploymentStyle]] = None
    ec2_tag_filter: Optional[Sequence[Ec2TagFilter]] = None
    ec2_tag_set: Optional[Sequence[Ec2TagSet]] = None
    ecs_service: Optional[Sequence[EcsService]] = None
    load_balancer_info: Optional[Sequence[LoadBalancerInfo]] = None
    on_premises_instance_tag_filter: Optional[Sequence[OnPremisesInstanceTagFilter]] = (
        None
    )
    outdated_instances_strategy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    trigger_configuration: Optional[Sequence[TriggerConfiguration]] = None
