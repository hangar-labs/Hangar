from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDmsReplicationSubnetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    replication_subnet_group_description: str
    replication_subnet_group_id: str
    subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dms_replication_subnet_group")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
