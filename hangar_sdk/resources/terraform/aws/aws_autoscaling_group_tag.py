from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Tag(AbstractTerraformBlock):
    key: str
    propagate_at_launch: bool
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag")


@define(kw_only=True, slots=False)
class AwsAutoscalingGroupTag(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_group_tag")
    tag: Optional[Sequence[Tag]] = None
