from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApigatewayv2RouteResponse(AbstractTerraformResource):
    _group: Any
    _top_name: str
    api_id: str
    route_id: str
    route_response_key: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apigatewayv2_route_response")
    model_selection_expression: Optional[str] = None
    response_models: Optional[Dict[str, str]] = None
