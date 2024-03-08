from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSsmMaintenanceWindow(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cutoff: int
    duration: int
    name: str
    schedule: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_maintenance_window")
    allow_unassociated_targets: Optional[bool] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    end_date: Optional[str] = None
    schedule_offset: Optional[int] = None
    schedule_timezone: Optional[str] = None
    start_date: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
