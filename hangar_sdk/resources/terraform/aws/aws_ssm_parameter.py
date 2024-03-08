from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSsmParameter(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_parameter")
    allowed_pattern: Optional[str] = None
    arn: Optional[str] = None
    data_type: Optional[str] = None
    description: Optional[str] = None
    insecure_value: Optional[str] = None
    key_id: Optional[str] = None
    overwrite: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tier: Optional[str] = None
    value: Optional[str] = None
