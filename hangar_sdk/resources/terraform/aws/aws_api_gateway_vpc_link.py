from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApiGatewayVpcLink(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    target_arns: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_api_gateway_vpc_link")
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
