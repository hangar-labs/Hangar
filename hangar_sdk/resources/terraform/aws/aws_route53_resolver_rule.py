from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class TargetIp(AbstractTerraformBlock):
    ip: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_ip")
    port: Optional[int] = None
    protocol: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53ResolverRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_name: str
    rule_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_rule")
    name: Optional[str] = None
    resolver_endpoint_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_ip: Optional[Sequence[TargetIp]] = None
    timeouts: Optional[Timeouts] = None
