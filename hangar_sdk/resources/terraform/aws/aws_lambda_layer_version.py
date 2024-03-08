from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLambdaLayerVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    layer_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_layer_version")
    compatible_architectures: Optional[Sequence[str]] = None
    compatible_runtimes: Optional[Sequence[str]] = None
    description: Optional[str] = None
    filename: Optional[str] = None
    license_info: Optional[str] = None
    s3_bucket: Optional[str] = None
    s3_key: Optional[str] = None
    s3_object_version: Optional[str] = None
    skip_destroy: Optional[bool] = None
    source_code_hash: Optional[str] = None
