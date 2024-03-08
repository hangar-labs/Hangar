from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayVpcAttachmentAccepter(AbstractTerraformResource):
    _group: Any
    _top_name: str
    transit_gateway_attachment_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_vpc_attachment_accepter"
    )
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    transit_gateway_default_route_table_association: Optional[bool] = None
    transit_gateway_default_route_table_propagation: Optional[bool] = None
