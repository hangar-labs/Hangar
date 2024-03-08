from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSsmDefaultPatchBaseline(AbstractTerraformResource):
    _group: Any
    _top_name: str
    baseline_id: str
    operating_system: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_default_patch_baseline")
