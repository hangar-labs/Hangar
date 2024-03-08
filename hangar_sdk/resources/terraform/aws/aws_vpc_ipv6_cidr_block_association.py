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
class AwsVpcIpv6CidrBlockAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ipv6_ipam_pool_id: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipv6_cidr_block_association")
    ipv6_cidr_block: Optional[str] = None
    ipv6_netmask_length: Optional[int] = None
    timeouts: Optional[Timeouts] = None
