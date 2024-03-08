from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsDocdbEngineVersion(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_docdb_engine_version")
    engine: Optional[str] = None
    parameter_group_family: Optional[str] = None
    preferred_versions: Optional[Sequence[str]] = None
    version: Optional[str] = None
