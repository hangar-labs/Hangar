from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamUserSshKey(AbstractTerraformResource):
    _group: Any
    _top_name: str
    encoding: str
    public_key: str
    username: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_user_ssh_key")
    status: Optional[str] = None
