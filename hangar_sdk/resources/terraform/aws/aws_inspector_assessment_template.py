from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EventSubscription(AbstractTerraformBlock):
    event: str
    topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="event_subscription")


@define(kw_only=True, slots=False)
class AwsInspectorAssessmentTemplate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    duration: int
    name: str
    rules_package_arns: Sequence[str]
    target_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_inspector_assessment_template")
    event_subscription: Optional[Sequence[EventSubscription]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
