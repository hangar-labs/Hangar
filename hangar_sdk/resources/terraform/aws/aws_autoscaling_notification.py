from typing import Any, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAutoscalingNotification(AbstractTerraformResource):
    _group: Any
    _top_name: str
    group_names: Sequence[str]
    notifications: Sequence[str]
    topic_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_notification")
