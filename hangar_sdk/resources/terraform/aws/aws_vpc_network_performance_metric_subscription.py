from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcNetworkPerformanceMetricSubscription(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination: str
    source: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_vpc_network_performance_metric_subscription"
    )
    metric: Optional[str] = None
    statistic: Optional[str] = None
