from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DnsOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dns_options")
    dns_record_ip_type: Optional[str] = None
    private_dns_only_for_inbound_resolver_endpoint: Optional[bool] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpcEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    service_name: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_endpoint")
    auto_accept: Optional[bool] = None
    dns_options: Optional[Sequence[DnsOptions]] = None
    ip_address_type: Optional[str] = None
    policy: Optional[str] = None
    private_dns_enabled: Optional[bool] = None
    route_table_ids: Optional[Sequence[str]] = None
    security_group_ids: Optional[Sequence[str]] = None
    subnet_ids: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_endpoint_type: Optional[str] = None
