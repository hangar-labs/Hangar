from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RoutingConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="routing_config")
    additional_version_weights: Optional[Dict[str, int]] = None


@define(kw_only=True, slots=False)
class AwsLambdaAlias(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    function_version: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_alias")
    description: Optional[str] = None
    routing_config: Optional[Sequence[RoutingConfig]] = None
