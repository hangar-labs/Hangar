from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSecurityGroupRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    from_port: int
    protocol: str
    security_group_id: str
    to_port: int
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_security_group_rule")
    cidr_blocks: Optional[Sequence[str]] = None
    description: Optional[str] = None
    ipv6_cidr_blocks: Optional[Sequence[str]] = None
    prefix_list_ids: Optional[Sequence[str]] = None
    source_security_group_id: Optional[str] = None
    terraform_self: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
