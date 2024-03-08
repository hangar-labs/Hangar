from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class TrafficSource(AbstractTerraformBlock):
    identifier: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="traffic_source")


@define(kw_only=True, slots=False)
class AwsAutoscalingTrafficSourceAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    autoscaling_group_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_autoscaling_traffic_source_attachment"
    )
    timeouts: Optional[Timeouts] = None
    traffic_source: Optional[Sequence[TrafficSource]] = None
