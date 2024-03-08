from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AccessLogs(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_logs")
    bucket_prefix: Optional[str] = None
    enabled: Optional[bool] = None
    interval: Optional[int] = None


@define(kw_only=True, slots=False)
class HealthCheck(AbstractTerraformBlock):
    healthy_threshold: int
    interval: int
    target: str
    timeout: int
    unhealthy_threshold: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="health_check")


@define(kw_only=True, slots=False)
class Listener(AbstractTerraformBlock):
    instance_port: int
    instance_protocol: str
    lb_port: int
    lb_protocol: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="listener")
    ssl_certificate_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsElb(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_elb")
    access_logs: Optional[Sequence[AccessLogs]] = None
    availability_zones: Optional[Sequence[str]] = None
    connection_draining: Optional[bool] = None
    connection_draining_timeout: Optional[int] = None
    cross_zone_load_balancing: Optional[bool] = None
    desync_mitigation_mode: Optional[str] = None
    health_check: Optional[Sequence[HealthCheck]] = None
    idle_timeout: Optional[int] = None
    instances: Optional[Sequence[str]] = None
    internal: Optional[bool] = None
    listener: Optional[Sequence[Listener]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    security_groups: Optional[Sequence[str]] = None
    source_security_group: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
