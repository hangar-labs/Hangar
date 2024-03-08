from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAlbTargetGroupAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    target_group_arn: str
    target_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_alb_target_group_attachment")
    availability_zone: Optional[str] = None
    port: Optional[int] = None
