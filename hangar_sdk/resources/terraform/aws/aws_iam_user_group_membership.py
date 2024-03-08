from typing import Any, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamUserGroupMembership(AbstractTerraformResource):
    _group: Any
    _top_name: str
    groups: Sequence[str]
    user: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_user_group_membership")
