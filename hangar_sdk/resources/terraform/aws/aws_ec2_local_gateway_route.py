from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2LocalGatewayRoute(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination_cidr_block: str
    local_gateway_route_table_id: str
    local_gateway_virtual_interface_group_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_local_gateway_route")
