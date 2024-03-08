from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Egress(AbstractTerraformBlock):
    action: str
    from_port: int
    protocol: str
    rule_no: int
    to_port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="egress")
    cidr_block: Optional[str] = None
    icmp_code: Optional[int] = None
    icmp_type: Optional[int] = None
    ipv6_cidr_block: Optional[str] = None


@define(kw_only=True, slots=False)
class Ingress(AbstractTerraformBlock):
    action: str
    from_port: int
    protocol: str
    rule_no: int
    to_port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ingress")
    cidr_block: Optional[str] = None
    icmp_code: Optional[int] = None
    icmp_type: Optional[int] = None
    ipv6_cidr_block: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDefaultNetworkAcl(AbstractTerraformResource):
    _group: Any
    _top_name: str
    default_network_acl_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_default_network_acl")
    egress: Optional[Sequence[Egress]] = None
    ingress: Optional[Sequence[Ingress]] = None
    subnet_ids: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
