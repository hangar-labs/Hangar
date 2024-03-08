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
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    read: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsAmiIds(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    owners: Sequence[str]
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ami_ids")
    executable_users: Optional[Sequence[str]] = None
    filter: Optional[Sequence[Filter]] = None
    include_deprecated: Optional[bool] = None
    name_regex: Optional[str] = None
    sort_ascending: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
