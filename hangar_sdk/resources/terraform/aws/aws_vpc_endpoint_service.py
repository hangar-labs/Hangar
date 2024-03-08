from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpcEndpointService(AbstractTerraformResource):
    _group: Any
    _top_name: str
    acceptance_required: bool
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_endpoint_service")
    allowed_principals: Optional[Sequence[str]] = None
    gateway_load_balancer_arns: Optional[Sequence[str]] = None
    network_load_balancer_arns: Optional[Sequence[str]] = None
    private_dns_name: Optional[str] = None
    supported_ip_address_types: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
