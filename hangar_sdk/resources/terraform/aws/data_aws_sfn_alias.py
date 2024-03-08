from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSfnAlias(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    name: str
    statemachine_arn: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_sfn_alias")
    description: Optional[str] = None
