from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailDatabase(AbstractTerraformResource):
    _group: Any
    _top_name: str
    blueprint_id: str
    bundle_id: str
    master_database_name: str
    master_password: str
    master_username: str
    relational_database_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_database")
    apply_immediately: Optional[bool] = None
    availability_zone: Optional[str] = None
    backup_retention_enabled: Optional[bool] = None
    final_snapshot_name: Optional[str] = None
    preferred_backup_window: Optional[str] = None
    preferred_maintenance_window: Optional[str] = None
    publicly_accessible: Optional[bool] = None
    skip_final_snapshot: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
