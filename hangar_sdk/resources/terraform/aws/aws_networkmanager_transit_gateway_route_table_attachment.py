from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsNetworkmanagerTransitGatewayRouteTableAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    peering_id: str
    transit_gateway_route_table_arn: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name",
        default="aws_networkmanager_transit_gateway_route_table_attachment",
    )
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
