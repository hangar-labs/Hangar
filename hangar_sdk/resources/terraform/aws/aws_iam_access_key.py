from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamAccessKey(AbstractTerraformResource):
    _group: Any
    _top_name: str
    user: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_access_key")
    pgp_key: Optional[str] = None
    status: Optional[str] = None
