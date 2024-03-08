from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class TagFilter(AbstractTerraformBlock):
    key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag_filter")
    values: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class ApplicationSource(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="application_source")
    cloudformation_stack_arn: Optional[str] = None
    tag_filter: Optional[Sequence[TagFilter]] = None


@define(kw_only=True, slots=False)
class CustomizedLoadMetricSpecification(AbstractTerraformBlock):
    metric_name: str
    namespace: str
    statistic: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="customized_load_metric_specification")
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[str] = None


@define(kw_only=True, slots=False)
class PredefinedLoadMetricSpecification(AbstractTerraformBlock):
    predefined_load_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_load_metric_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class CustomizedScalingMetricSpecification(AbstractTerraformBlock):
    metric_name: str
    namespace: str
    statistic: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="customized_scaling_metric_specification")
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[str] = None


@define(kw_only=True, slots=False)
class PredefinedScalingMetricSpecification(AbstractTerraformBlock):
    predefined_scaling_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_scaling_metric_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class TargetTrackingConfiguration(AbstractTerraformBlock):
    target_value: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_tracking_configuration")
    customized_scaling_metric_specification: Optional[
        Sequence[CustomizedScalingMetricSpecification]
    ] = None
    disable_scale_in: Optional[bool] = None
    estimated_instance_warmup: Optional[int] = None
    predefined_scaling_metric_specification: Optional[
        Sequence[PredefinedScalingMetricSpecification]
    ] = None
    scale_in_cooldown: Optional[int] = None
    scale_out_cooldown: Optional[int] = None


@define(kw_only=True, slots=False)
class ScalingInstruction(AbstractTerraformBlock):
    max_capacity: int
    min_capacity: int
    resource_id: str
    scalable_dimension: str
    service_namespace: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scaling_instruction")
    customized_load_metric_specification: Optional[
        Sequence[CustomizedLoadMetricSpecification]
    ] = None
    disable_dynamic_scaling: Optional[bool] = None
    predefined_load_metric_specification: Optional[
        Sequence[PredefinedLoadMetricSpecification]
    ] = None
    predictive_scaling_max_capacity_behavior: Optional[str] = None
    predictive_scaling_max_capacity_buffer: Optional[int] = None
    predictive_scaling_mode: Optional[str] = None
    scaling_policy_update_behavior: Optional[str] = None
    scheduled_action_buffer_time: Optional[int] = None
    target_tracking_configuration: Optional[Sequence[TargetTrackingConfiguration]] = (
        None
    )


@define(kw_only=True, slots=False)
class AwsAutoscalingplansScalingPlan(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscalingplans_scaling_plan")
    application_source: Optional[Sequence[ApplicationSource]] = None
    scaling_instruction: Optional[Sequence[ScalingInstruction]] = None
