from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsDmsReplicationSubnetGroup(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    replication_subnet_group_id: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_dms_replication_subnet_group")
    tags: Optional[Dict[str, str]] = None
