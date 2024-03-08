from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSsmParametersByPath(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    path: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ssm_parameters_by_path")
    recursive: Optional[bool] = None
    with_decryption: Optional[bool] = None
