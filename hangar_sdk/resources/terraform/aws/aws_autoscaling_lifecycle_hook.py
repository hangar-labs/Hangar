from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAutoscalingLifecycleHook(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    lifecycle_transition: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_lifecycle_hook")
    default_result: Optional[str] = None
    heartbeat_timeout: Optional[int] = None
    notification_metadata: Optional[str] = None
    notification_target_arn: Optional[str] = None
    role_arn: Optional[str] = None
