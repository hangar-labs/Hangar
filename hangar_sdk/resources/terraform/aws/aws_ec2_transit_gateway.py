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
class AwsEc2TransitGateway(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_transit_gateway")
    amazon_side_asn: Optional[int] = None
    auto_accept_shared_attachments: Optional[str] = None
    default_route_table_association: Optional[str] = None
    default_route_table_propagation: Optional[str] = None
    description: Optional[str] = None
    dns_support: Optional[str] = None
    multicast_support: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    transit_gateway_cidr_blocks: Optional[Sequence[str]] = None
    vpn_ecmp_support: Optional[str] = None
