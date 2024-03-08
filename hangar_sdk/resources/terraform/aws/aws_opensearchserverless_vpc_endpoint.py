from typing import Any, Optional, Sequence

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
class AwsOpensearchserverlessVpcEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    subnet_ids: Sequence[str]
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_opensearchserverless_vpc_endpoint")
    security_group_ids: Optional[Sequence[str]] = None
    timeouts: Optional[Timeouts] = None
