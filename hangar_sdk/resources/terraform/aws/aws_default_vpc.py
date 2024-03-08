from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDefaultVpc(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_default_vpc")
    assign_generated_ipv6_cidr_block: Optional[bool] = None
    enable_dns_hostnames: Optional[bool] = None
    enable_dns_support: Optional[bool] = None
    enable_network_address_usage_metrics: Optional[bool] = None
    force_destroy: Optional[bool] = None
    ipv6_cidr_block: Optional[str] = None
    ipv6_cidr_block_network_border_group: Optional[str] = None
    ipv6_ipam_pool_id: Optional[str] = None
    ipv6_netmask_length: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
