from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayConnectPeer(AbstractTerraformResource):
    _group: Any
    _top_name: str
    inside_cidr_blocks: Sequence[str]
    peer_address: str
    transit_gateway_attachment_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_transit_gateway_connect_peer")
    bgp_asn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    transit_gateway_address: Optional[str] = None
