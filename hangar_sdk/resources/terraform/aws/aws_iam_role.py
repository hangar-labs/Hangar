from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class InlinePolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="inline_policy")
    name: Optional[str] = None
    policy: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsIamRole(AbstractTerraformResource):
    _group: Any
    _top_name: str
    assume_role_policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_role")
    description: Optional[str] = None
    force_detach_policies: Optional[bool] = None
    inline_policy: Optional[Sequence[InlinePolicy]] = None
    managed_policy_arns: Optional[Sequence[str]] = None
    max_session_duration: Optional[int] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    path: Optional[str] = None
    permissions_boundary: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
