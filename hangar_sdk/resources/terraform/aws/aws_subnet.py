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
class AwsSubnet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_subnet")
    assign_ipv6_address_on_creation: Optional[bool] = None
    availability_zone: Optional[str] = None
    availability_zone_id: Optional[str] = None
    cidr_block: Optional[str] = None
    customer_owned_ipv4_pool: Optional[str] = None
    enable_dns64: Optional[bool] = None
    enable_lni_at_device_index: Optional[int] = None
    enable_resource_name_dns_a_record_on_launch: Optional[bool] = None
    enable_resource_name_dns_aaaa_record_on_launch: Optional[bool] = None
    ipv6_cidr_block: Optional[str] = None
    ipv6_native: Optional[bool] = None
    map_customer_owned_ip_on_launch: Optional[bool] = None
    map_public_ip_on_launch: Optional[bool] = None
    outpost_arn: Optional[str] = None
    private_dns_hostname_type_on_launch: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
