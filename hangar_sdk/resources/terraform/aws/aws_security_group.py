from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Egress(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="egress")
    protocol: Optional[str] = None
    cidr_blocks: Optional[Sequence[str]] = None
    from_port: Optional[int] = None
    description: Optional[str] = None
    terraform_self: Optional[bool] = None
    prefix_list_ids: Optional[Sequence[str]] = None
    security_groups: Optional[Sequence[str]] = None
    to_port: Optional[int] = None
    ipv6_cidr_blocks: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Ingress(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ingress")
    security_groups: Optional[Sequence[str]] = None
    to_port: Optional[int] = None
    protocol: Optional[str] = None
    cidr_blocks: Optional[Sequence[str]] = None
    description: Optional[str] = None
    from_port: Optional[int] = None
    prefix_list_ids: Optional[Sequence[str]] = None
    ipv6_cidr_blocks: Optional[Sequence[str]] = None
    terraform_self: Optional[bool] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSecurityGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_security_group")
    description: Optional[str] = None
    egress: Optional[Sequence[Egress]] = None
    ingress: Optional[Sequence[Ingress]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    revoke_rules_on_delete: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_id: Optional[str] = None
