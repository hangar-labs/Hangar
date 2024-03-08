from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class StepAdjustment(AbstractTerraformBlock):
    scaling_adjustment: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="step_adjustment")
    metric_interval_lower_bound: Optional[str] = None
    metric_interval_upper_bound: Optional[str] = None


@define(kw_only=True, slots=False)
class StepScalingPolicyConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="step_scaling_policy_configuration")
    adjustment_type: Optional[str] = None
    cooldown: Optional[int] = None
    metric_aggregation_type: Optional[str] = None
    min_adjustment_magnitude: Optional[int] = None
    step_adjustment: Optional[Sequence[StepAdjustment]] = None


@define(kw_only=True, slots=False)
class Dimensions(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dimensions")


@define(kw_only=True, slots=False)
class Dimensions(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dimensions")


@define(kw_only=True, slots=False)
class Metric(AbstractTerraformBlock):
    metric_name: str
    namespace: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric")
    dimensions: Optional[Sequence[Dimensions]] = None


@define(kw_only=True, slots=False)
class MetricStat(AbstractTerraformBlock):
    stat: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_stat")
    metric: Optional[Sequence[Metric]] = None
    unit: Optional[str] = None


@define(kw_only=True, slots=False)
class Metrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metrics")
    expression: Optional[str] = None
    label: Optional[str] = None
    metric_stat: Optional[Sequence[MetricStat]] = None
    return_data: Optional[bool] = None


@define(kw_only=True, slots=False)
class CustomizedMetricSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="customized_metric_specification")
    dimensions: Optional[Sequence[Dimensions]] = None
    metric_name: Optional[str] = None
    metrics: Optional[Sequence[Metrics]] = None
    namespace: Optional[str] = None
    statistic: Optional[str] = None
    unit: Optional[str] = None


@define(kw_only=True, slots=False)
class PredefinedMetricSpecification(AbstractTerraformBlock):
    predefined_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_metric_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class TargetTrackingScalingPolicyConfiguration(AbstractTerraformBlock):
    target_value: int
    _block_type: str = "block"
    _name: str = field(
        alias="_name", default="target_tracking_scaling_policy_configuration"
    )
    customized_metric_specification: Optional[
        Sequence[CustomizedMetricSpecification]
    ] = None
    disable_scale_in: Optional[bool] = None
    predefined_metric_specification: Optional[
        Sequence[PredefinedMetricSpecification]
    ] = None
    scale_in_cooldown: Optional[int] = None
    scale_out_cooldown: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsAppautoscalingPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    resource_id: str
    scalable_dimension: str
    service_namespace: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_appautoscaling_policy")
    policy_type: Optional[str] = None
    step_scaling_policy_configuration: Optional[
        Sequence[StepScalingPolicyConfiguration]
    ] = None
    target_tracking_scaling_policy_configuration: Optional[
        Sequence[TargetTrackingScalingPolicyConfiguration]
    ] = None
