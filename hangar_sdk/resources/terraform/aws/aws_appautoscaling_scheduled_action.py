from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ScalableTargetAction(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scalable_target_action")
    max_capacity: Optional[str] = None
    min_capacity: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsAppautoscalingScheduledAction(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    resource_id: str
    scalable_dimension: str
    schedule: str
    service_namespace: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_appautoscaling_scheduled_action")
    end_time: Optional[str] = None
    scalable_target_action: Optional[Sequence[ScalableTargetAction]] = None
    start_time: Optional[str] = None
    timezone: Optional[str] = None
