from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamRolePolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    role: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_role_policy")
    name: Optional[str] = None
    name_prefix: Optional[str] = None
