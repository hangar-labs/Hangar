from typing import Any, Optional

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
class AwsRouteTableAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    route_table_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route_table_association")
    gateway_id: Optional[str] = None
    subnet_id: Optional[str] = None
    timeouts: Optional[Timeouts] = None
