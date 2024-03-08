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
class DataAwsVpcPeeringConnection(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_vpc_peering_connection")
    cidr_block: Optional[str] = None
    filter: Optional[Sequence[Filter]] = None
    owner_id: Optional[str] = None
    peer_cidr_block: Optional[str] = None
    peer_owner_id: Optional[str] = None
    peer_region: Optional[str] = None
    peer_vpc_id: Optional[str] = None
    region: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_id: Optional[str] = None
