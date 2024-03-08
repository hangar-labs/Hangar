from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsLocationRouteCalculator(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    calculator_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_location_route_calculator")
    tags: Optional[Dict[str, str]] = None
