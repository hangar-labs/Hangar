from typing import Any, Dict, Optional

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
class AwsVpcIpamPool(AbstractTerraformResource):
    _group: Any
    _top_name: str
    address_family: str
    ipam_scope_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipam_pool")
    allocation_default_netmask_length: Optional[int] = None
    allocation_max_netmask_length: Optional[int] = None
    allocation_min_netmask_length: Optional[int] = None
    allocation_resource_tags: Optional[Dict[str, str]] = None
    auto_import: Optional[bool] = None
    aws_service: Optional[str] = None
    description: Optional[str] = None
    locale: Optional[str] = None
    public_ip_source: Optional[str] = None
    publicly_advertisable: Optional[bool] = None
    source_ipam_pool_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
