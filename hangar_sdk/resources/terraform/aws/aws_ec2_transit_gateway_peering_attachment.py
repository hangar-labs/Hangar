from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayPeeringAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    peer_region: str
    peer_transit_gateway_id: str
    transit_gateway_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_peering_attachment"
    )
    peer_account_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
