from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamPolicyAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    policy_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_policy_attachment")
    groups: Optional[Sequence[str]] = None
    roles: Optional[Sequence[str]] = None
    users: Optional[Sequence[str]] = None
