from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsDbSnapshot(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_db_snapshot")
    db_instance_identifier: Optional[str] = None
    db_snapshot_identifier: Optional[str] = None
    include_public: Optional[bool] = None
    include_shared: Optional[bool] = None
    most_recent: Optional[bool] = None
    snapshot_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
