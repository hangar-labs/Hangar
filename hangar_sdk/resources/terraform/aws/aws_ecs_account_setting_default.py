from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEcsAccountSettingDefault(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    value: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_account_setting_default")
