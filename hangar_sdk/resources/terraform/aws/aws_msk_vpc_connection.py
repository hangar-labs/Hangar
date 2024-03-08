from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsMskVpcConnection(AbstractTerraformResource):
    _group: Any
    _top_name: str
    authentication: str
    client_subnets: Sequence[str]
    security_groups: Sequence[str]
    target_cluster_arn: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_msk_vpc_connection")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
