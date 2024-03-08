from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSecretsmanagerRandomPassword(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_secretsmanager_random_password")
    exclude_characters: Optional[str] = None
    exclude_lowercase: Optional[bool] = None
    exclude_numbers: Optional[bool] = None
    exclude_punctuation: Optional[bool] = None
    exclude_uppercase: Optional[bool] = None
    include_space: Optional[bool] = None
    password_length: Optional[int] = None
    require_each_included_type: Optional[bool] = None
