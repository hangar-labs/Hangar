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
class AwsDbProxyEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_proxy_endpoint_name: str
    db_proxy_name: str
    vpc_subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_proxy_endpoint")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_role: Optional[str] = None
    timeouts: Optional[Timeouts] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
