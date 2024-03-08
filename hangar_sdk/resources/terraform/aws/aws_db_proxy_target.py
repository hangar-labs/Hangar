from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDbProxyTarget(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_proxy_name: str
    target_group_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_proxy_target")
    db_cluster_identifier: Optional[str] = None
    db_instance_identifier: Optional[str] = None
