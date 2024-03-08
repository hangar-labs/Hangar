from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSnsTopicSubscription(AbstractTerraformResource):
    _group: Any
    _top_name: str
    endpoint: str
    protocol: str
    topic_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sns_topic_subscription")
    confirmation_timeout_in_minutes: Optional[int] = None
    delivery_policy: Optional[str] = None
    endpoint_auto_confirms: Optional[bool] = None
    filter_policy: Optional[str] = None
    filter_policy_scope: Optional[str] = None
    raw_message_delivery: Optional[bool] = None
    redrive_policy: Optional[str] = None
    replay_policy: Optional[str] = None
    subscription_role_arn: Optional[str] = None
