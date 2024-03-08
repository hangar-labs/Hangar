from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSsmPatchBaseline(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    owner: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ssm_patch_baseline")
    default_baseline: Optional[bool] = None
    name_prefix: Optional[str] = None
    operating_system: Optional[str] = None
