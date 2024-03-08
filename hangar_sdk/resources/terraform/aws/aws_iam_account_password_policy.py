from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamAccountPasswordPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_account_password_policy")
    allow_users_to_change_password: Optional[bool] = None
    hard_expiry: Optional[bool] = None
    max_password_age: Optional[int] = None
    minimum_password_length: Optional[int] = None
    password_reuse_prevention: Optional[int] = None
    require_lowercase_characters: Optional[bool] = None
    require_numbers: Optional[bool] = None
    require_symbols: Optional[bool] = None
    require_uppercase_characters: Optional[bool] = None
