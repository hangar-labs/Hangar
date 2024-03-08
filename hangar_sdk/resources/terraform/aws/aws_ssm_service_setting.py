from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSsmServiceSetting(AbstractTerraformResource):
    _group: Any
    _top_name: str
    setting_id: str
    setting_value: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_service_setting")
