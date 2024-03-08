from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class IpAddress(AbstractTerraformBlock):
    subnet_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ip_address")
    ip: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53ResolverEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    direction: str
    security_group_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_endpoint")
    ip_address: Optional[Sequence[IpAddress]] = None
    name: Optional[str] = None
    protocols: Optional[Sequence[str]] = None
    resolver_endpoint_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
