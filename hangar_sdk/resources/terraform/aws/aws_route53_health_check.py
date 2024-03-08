from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53HealthCheck(AbstractTerraformResource):
    _group: Any
    _top_name: str
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_health_check")
    child_health_threshold: Optional[int] = None
    child_healthchecks: Optional[Sequence[str]] = None
    cloudwatch_alarm_name: Optional[str] = None
    cloudwatch_alarm_region: Optional[str] = None
    disabled: Optional[bool] = None
    enable_sni: Optional[bool] = None
    failure_threshold: Optional[int] = None
    fqdn: Optional[str] = None
    insufficient_data_health_status: Optional[str] = None
    invert_healthcheck: Optional[bool] = None
    ip_address: Optional[str] = None
    measure_latency: Optional[bool] = None
    port: Optional[int] = None
    reference_name: Optional[str] = None
    regions: Optional[Sequence[str]] = None
    request_interval: Optional[int] = None
    resource_path: Optional[str] = None
    routing_control_arn: Optional[str] = None
    search_string: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
