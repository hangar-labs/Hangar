from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


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
class MetricDataQueries(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_data_queries")
    expression: Optional[str] = None
    label: Optional[str] = None
    metric_stat: Optional[Sequence[MetricStat]] = None
    return_data: Optional[bool] = None


@define(kw_only=True, slots=False)
class CustomizedCapacityMetricSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(
        alias="_name", default="customized_capacity_metric_specification"
    )
    metric_data_queries: Optional[Sequence[MetricDataQueries]] = None


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
class MetricDataQueries(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_data_queries")
    expression: Optional[str] = None
    label: Optional[str] = None
    metric_stat: Optional[Sequence[MetricStat]] = None
    return_data: Optional[bool] = None


@define(kw_only=True, slots=False)
class CustomizedLoadMetricSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="customized_load_metric_specification")
    metric_data_queries: Optional[Sequence[MetricDataQueries]] = None


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
class MetricDataQueries(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_data_queries")
    expression: Optional[str] = None
    label: Optional[str] = None
    metric_stat: Optional[Sequence[MetricStat]] = None
    return_data: Optional[bool] = None


@define(kw_only=True, slots=False)
class CustomizedScalingMetricSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="customized_scaling_metric_specification")
    metric_data_queries: Optional[Sequence[MetricDataQueries]] = None


@define(kw_only=True, slots=False)
class PredefinedLoadMetricSpecification(AbstractTerraformBlock):
    predefined_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_load_metric_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class PredefinedMetricPairSpecification(AbstractTerraformBlock):
    predefined_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_metric_pair_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class PredefinedScalingMetricSpecification(AbstractTerraformBlock):
    predefined_metric_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predefined_scaling_metric_specification")
    resource_label: Optional[str] = None


@define(kw_only=True, slots=False)
class MetricSpecification(AbstractTerraformBlock):
    target_value: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_specification")
    customized_capacity_metric_specification: Optional[
        Sequence[CustomizedCapacityMetricSpecification]
    ] = None
    customized_load_metric_specification: Optional[
        Sequence[CustomizedLoadMetricSpecification]
    ] = None
    customized_scaling_metric_specification: Optional[
        Sequence[CustomizedScalingMetricSpecification]
    ] = None
    predefined_load_metric_specification: Optional[
        Sequence[PredefinedLoadMetricSpecification]
    ] = None
    predefined_metric_pair_specification: Optional[
        Sequence[PredefinedMetricPairSpecification]
    ] = None
    predefined_scaling_metric_specification: Optional[
        Sequence[PredefinedScalingMetricSpecification]
    ] = None


@define(kw_only=True, slots=False)
class PredictiveScalingConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="predictive_scaling_configuration")
    max_capacity_breach_behavior: Optional[str] = None
    max_capacity_buffer: Optional[str] = None
    metric_specification: Optional[Sequence[MetricSpecification]] = None
    mode: Optional[str] = None
    scheduling_buffer_time: Optional[str] = None


@define(kw_only=True, slots=False)
class StepAdjustment(AbstractTerraformBlock):
    scaling_adjustment: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="step_adjustment")
    metric_interval_lower_bound: Optional[str] = None
    metric_interval_upper_bound: Optional[str] = None


@define(kw_only=True, slots=False)
class MetricDimension(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metric_dimension")


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
    metric_dimension: Optional[Sequence[MetricDimension]] = None
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
class TargetTrackingConfiguration(AbstractTerraformBlock):
    target_value: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_tracking_configuration")
    customized_metric_specification: Optional[
        Sequence[CustomizedMetricSpecification]
    ] = None
    disable_scale_in: Optional[bool] = None
    predefined_metric_specification: Optional[
        Sequence[PredefinedMetricSpecification]
    ] = None


@define(kw_only=True, slots=False)
class AwsAutoscalingPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_policy")
    adjustment_type: Optional[str] = None
    cooldown: Optional[int] = None
    enabled: Optional[bool] = None
    estimated_instance_warmup: Optional[int] = None
    metric_aggregation_type: Optional[str] = None
    min_adjustment_magnitude: Optional[int] = None
    policy_type: Optional[str] = None
    predictive_scaling_configuration: Optional[
        Sequence[PredictiveScalingConfiguration]
    ] = None
    scaling_adjustment: Optional[int] = None
    step_adjustment: Optional[Sequence[StepAdjustment]] = None
    target_tracking_configuration: Optional[Sequence[TargetTrackingConfiguration]] = (
        None
    )
