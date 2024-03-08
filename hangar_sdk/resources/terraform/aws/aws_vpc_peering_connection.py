from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Accepter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="accepter")
    allow_remote_vpc_dns_resolution: Optional[bool] = None


@define(kw_only=True, slots=False)
class Requester(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="requester")
    allow_remote_vpc_dns_resolution: Optional[bool] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpcPeeringConnection(AbstractTerraformResource):
    _group: Any
    _top_name: str
    peer_vpc_id: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_peering_connection")
    accepter: Optional[Sequence[Accepter]] = None
    auto_accept: Optional[bool] = None
    peer_owner_id: Optional[str] = None
    peer_region: Optional[str] = None
    requester: Optional[Sequence[Requester]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
