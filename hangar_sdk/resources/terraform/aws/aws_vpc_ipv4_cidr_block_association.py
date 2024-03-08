from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpcIpv4CidrBlockAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipv4_cidr_block_association")
    cidr_block: Optional[str] = None
    ipv4_ipam_pool_id: Optional[str] = None
    ipv4_netmask_length: Optional[int] = None
    timeouts: Optional[Timeouts] = None
