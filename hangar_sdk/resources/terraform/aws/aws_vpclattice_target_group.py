from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Matcher(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="matcher")
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class HealthCheck(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="health_check")
    enabled: Optional[bool] = None
    health_check_interval_seconds: Optional[int] = None
    health_check_timeout_seconds: Optional[int] = None
    healthy_threshold_count: Optional[int] = None
    matcher: Optional[Sequence[Matcher]] = None
    path: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    protocol_version: Optional[str] = None
    unhealthy_threshold_count: Optional[int] = None


@define(kw_only=True, slots=False)
class Config(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="config")
    health_check: Optional[Sequence[HealthCheck]] = None
    ip_address_type: Optional[str] = None
    lambda_event_structure_version: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    protocol_version: Optional[str] = None
    vpc_identifier: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpclatticeTargetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpclattice_target_group")
    config: Optional[Sequence[Config]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
