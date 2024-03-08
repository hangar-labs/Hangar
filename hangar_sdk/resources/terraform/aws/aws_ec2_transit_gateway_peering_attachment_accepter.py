from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayPeeringAttachmentAccepter(AbstractTerraformResource):
    _group: Any
    _top_name: str
    transit_gateway_attachment_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_peering_attachment_accepter"
    )
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
