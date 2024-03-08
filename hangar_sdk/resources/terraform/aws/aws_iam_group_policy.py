from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamGroupPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    terraform_group: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_group_policy")
    name: Optional[str] = None
    name_prefix: Optional[str] = None
