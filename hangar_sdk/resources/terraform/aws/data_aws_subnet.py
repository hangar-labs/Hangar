from typing import Any, Dict, Optional, Sequence

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
class DataAwsSubnet(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_subnet")
    availability_zone: Optional[str] = None
    availability_zone_id: Optional[str] = None
    cidr_block: Optional[str] = None
    default_for_az: Optional[bool] = None
    filter: Optional[Sequence[Filter]] = None
    ipv6_cidr_block: Optional[str] = None
    state: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_id: Optional[str] = None
