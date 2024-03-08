from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsNatGateway(AbstractTerraformResource):
    _group: Any
    _top_name: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_nat_gateway")
    allocation_id: Optional[str] = None
    connectivity_type: Optional[str] = None
    private_ip: Optional[str] = None
    secondary_allocation_ids: Optional[Sequence[str]] = None
    secondary_private_ip_address_count: Optional[int] = None
    secondary_private_ip_addresses: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
