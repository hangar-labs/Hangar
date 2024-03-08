from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcEndpointRouteTableAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    route_table_id: str
    vpc_endpoint_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_vpc_endpoint_route_table_association"
    )
