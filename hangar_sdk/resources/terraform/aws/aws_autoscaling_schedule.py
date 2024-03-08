from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAutoscalingSchedule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    scheduled_action_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_schedule")
    desired_capacity: Optional[int] = None
    end_time: Optional[str] = None
    max_size: Optional[int] = None
    min_size: Optional[int] = None
    recurrence: Optional[str] = None
    start_time: Optional[str] = None
    time_zone: Optional[str] = None
