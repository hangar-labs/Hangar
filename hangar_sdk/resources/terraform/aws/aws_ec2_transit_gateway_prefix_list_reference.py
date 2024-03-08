from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayPrefixListReference(AbstractTerraformResource):
    _group: Any
    _top_name: str
    prefix_list_id: str
    transit_gateway_route_table_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_prefix_list_reference"
    )
    blackhole: Optional[bool] = None
    transit_gateway_attachment_id: Optional[str] = None
