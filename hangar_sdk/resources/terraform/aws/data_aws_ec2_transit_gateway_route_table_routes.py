from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")


@define(kw_only=True, slots=False)
class DataAwsEc2TransitGatewayRouteTableRoutes(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    transit_gateway_route_table_id: str
    _block_type: str = "datasource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_route_table_routes"
    )
    filter: Optional[Sequence[Filter]] = None
