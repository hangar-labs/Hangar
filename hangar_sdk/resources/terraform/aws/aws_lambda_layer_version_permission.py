from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLambdaLayerVersionPermission(AbstractTerraformResource):
    _group: Any
    _top_name: str
    action: str
    layer_name: str
    principal: str
    statement_id: str
    version_number: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_layer_version_permission")
    organization_id: Optional[str] = None
    skip_destroy: Optional[bool] = None
