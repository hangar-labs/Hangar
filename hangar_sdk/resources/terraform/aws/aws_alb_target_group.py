from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class HealthCheck(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="health_check")
    enabled: Optional[bool] = None
    healthy_threshold: Optional[int] = None
    interval: Optional[int] = None
    matcher: Optional[str] = None
    path: Optional[str] = None
    port: Optional[str] = None
    protocol: Optional[str] = None
    timeout: Optional[int] = None
    unhealthy_threshold: Optional[int] = None


@define(kw_only=True, slots=False)
class Stickiness(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="stickiness")
    cookie_duration: Optional[int] = None
    cookie_name: Optional[str] = None
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class TargetFailover(AbstractTerraformBlock):
    on_deregistration: str
    on_unhealthy: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_failover")


@define(kw_only=True, slots=False)
class TargetHealthState(AbstractTerraformBlock):
    enable_unhealthy_connection_termination: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_health_state")


@define(kw_only=True, slots=False)
class AwsAlbTargetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_alb_target_group")
    connection_termination: Optional[bool] = None
    deregistration_delay: Optional[str] = None
    health_check: Optional[Sequence[HealthCheck]] = None
    ip_address_type: Optional[str] = None
    lambda_multi_value_headers_enabled: Optional[bool] = None
    load_balancing_algorithm_type: Optional[str] = None
    load_balancing_anomaly_mitigation: Optional[str] = None
    load_balancing_cross_zone_enabled: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    port: Optional[int] = None
    preserve_client_ip: Optional[str] = None
    protocol: Optional[str] = None
    protocol_version: Optional[str] = None
    proxy_protocol_v2: Optional[bool] = None
    slow_start: Optional[int] = None
    stickiness: Optional[Sequence[Stickiness]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_failover: Optional[Sequence[TargetFailover]] = None
    target_health_state: Optional[Sequence[TargetHealthState]] = None
    target_type: Optional[str] = None
    vpc_id: Optional[str] = None
