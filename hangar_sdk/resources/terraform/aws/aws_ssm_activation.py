from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSsmActivation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    iam_role: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_activation")
    description: Optional[str] = None
    expiration_date: Optional[str] = None
    name: Optional[str] = None
    registration_limit: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
