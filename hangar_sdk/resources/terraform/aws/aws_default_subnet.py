from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDefaultSubnet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_default_subnet")
    assign_ipv6_address_on_creation: Optional[bool] = None
    customer_owned_ipv4_pool: Optional[str] = None
    enable_dns64: Optional[bool] = None
    enable_resource_name_dns_a_record_on_launch: Optional[bool] = None
    enable_resource_name_dns_aaaa_record_on_launch: Optional[bool] = None
    force_destroy: Optional[bool] = None
    ipv6_cidr_block: Optional[str] = None
    ipv6_native: Optional[bool] = None
    map_customer_owned_ip_on_launch: Optional[bool] = None
    map_public_ip_on_launch: Optional[bool] = None
    private_dns_hostname_type_on_launch: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
