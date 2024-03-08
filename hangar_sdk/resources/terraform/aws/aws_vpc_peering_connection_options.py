from typing import Any, Optional, Sequence

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
class AwsVpcPeeringConnectionOptions(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vpc_peering_connection_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_peering_connection_options")
    accepter: Optional[Sequence[Accepter]] = None
    requester: Optional[Sequence[Requester]] = None
