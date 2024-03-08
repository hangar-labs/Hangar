from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsApigatewayv2VpcLink(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    vpc_link_id: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_apigatewayv2_vpc_link")
    tags: Optional[Dict[str, str]] = None
