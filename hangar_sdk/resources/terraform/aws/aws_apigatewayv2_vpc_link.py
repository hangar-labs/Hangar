from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApigatewayv2VpcLink(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    security_group_ids: Sequence[str]
    subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apigatewayv2_vpc_link")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
