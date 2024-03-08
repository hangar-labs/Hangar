from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpnGatewayRoutePropagation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    route_table_id: str
    vpn_gateway_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpn_gateway_route_propagation")
    timeouts: Optional[Timeouts] = None
