from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")


@define(kw_only=True, slots=False)
class DataAwsRdsEngineVersion(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    engine: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_rds_engine_version")
    default_only: Optional[bool] = None
    filter: Optional[Sequence[Filter]] = None
    include_all: Optional[bool] = None
    latest: Optional[bool] = None
    parameter_group_family: Optional[str] = None
    preferred_major_targets: Optional[Sequence[str]] = None
    preferred_upgrade_targets: Optional[Sequence[str]] = None
    preferred_versions: Optional[Sequence[str]] = None
    version: Optional[str] = None
