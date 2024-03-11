from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Dict,Optional,Sequence


@define(kw_only=True, slots=False)
class AccessLogs(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_logs")
    enabled: Optional[bool] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class ConnectionLogs(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="connection_logs")
    enabled: Optional[bool] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class SubnetMapping(AbstractTerraformBlock):
    subnet_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="subnet_mapping")
    allocation_id: Optional[str] = None
    ipv6_address: Optional[str] = None
    private_ipv4_address: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLb(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lb")
    access_logs: Optional[Sequence[AccessLogs]] = None
    connection_logs: Optional[Sequence[ConnectionLogs]] = None
    customer_owned_ipv4_pool: Optional[str] = None
    desync_mitigation_mode: Optional[str] = None
    dns_record_client_routing_policy: Optional[str] = None
    drop_invalid_header_fields: Optional[bool] = None
    enable_cross_zone_load_balancing: Optional[bool] = None
    enable_deletion_protection: Optional[bool] = None
    enable_http2: Optional[bool] = None
    enable_tls_version_and_cipher_suite_headers: Optional[bool] = None
    enable_waf_fail_open: Optional[bool] = None
    enable_xff_client_port: Optional[bool] = None
    enforce_security_group_inbound_rules_on_private_link_traffic: Optional[str] = None
    idle_timeout: Optional[int] = None
    internal: Optional[bool] = None
    ip_address_type: Optional[str] = None
    load_balancer_type: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    preserve_host_header: Optional[bool] = None
    security_groups: Optional[Sequence[str]] = None
    subnet_mapping: Optional[Sequence[SubnetMapping]] = None
    subnets: Optional[Sequence[str]] = None
    tags: Optional[Dict[str,str]] = None
    tags_all: Optional[Dict[str,str]] = None
    timeouts: Optional[Timeouts] = None
    xff_header_processing_mode: Optional[str] = None


