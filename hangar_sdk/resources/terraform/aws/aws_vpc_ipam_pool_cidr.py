from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CidrAuthorizationContext(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cidr_authorization_context")
    message: Optional[str] = None
    signature: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpcIpamPoolCidr(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ipam_pool_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipam_pool_cidr")
    cidr: Optional[str] = None
    cidr_authorization_context: Optional[Sequence[CidrAuthorizationContext]] = None
    netmask_length: Optional[int] = None
    timeouts: Optional[Timeouts] = None
