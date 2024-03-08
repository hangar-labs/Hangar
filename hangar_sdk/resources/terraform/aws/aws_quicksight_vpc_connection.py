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
class AwsQuicksightVpcConnection(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    role_arn: str
    security_group_ids: Sequence[str]
    subnet_ids: Sequence[str]
    vpc_connection_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_quicksight_vpc_connection")
    aws_account_id: Optional[str] = None
    dns_resolvers: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
