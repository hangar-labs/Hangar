from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAutoscalingAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_attachment")
    elb: Optional[str] = None
    lb_target_group_arn: Optional[str] = None
