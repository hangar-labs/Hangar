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
class DataAwsVpcIpamPoolCidrs(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    ipam_pool_id: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_vpc_ipam_pool_cidrs")
    filter: Optional[Sequence[Filter]] = None
    timeouts: Optional[Timeouts] = None
