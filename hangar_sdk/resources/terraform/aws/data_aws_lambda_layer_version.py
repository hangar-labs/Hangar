from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsLambdaLayerVersion(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    layer_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_lambda_layer_version")
    compatible_architecture: Optional[str] = None
    compatible_runtime: Optional[str] = None
    version: Optional[int] = None
