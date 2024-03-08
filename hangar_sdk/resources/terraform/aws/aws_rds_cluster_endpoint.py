from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRdsClusterEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_endpoint_identifier: str
    cluster_identifier: str
    custom_endpoint_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_cluster_endpoint")
    excluded_members: Optional[Sequence[str]] = None
    static_members: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
