from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsIamUserSshKey(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    encoding: str
    ssh_public_key_id: str
    username: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_user_ssh_key")
