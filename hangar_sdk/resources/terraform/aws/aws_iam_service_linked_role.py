from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamServiceLinkedRole(AbstractTerraformResource):
    _group: Any
    _top_name: str
    aws_service_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_service_linked_role")
    custom_suffix: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
