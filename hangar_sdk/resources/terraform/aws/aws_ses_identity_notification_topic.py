from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSesIdentityNotificationTopic(AbstractTerraformResource):
    _group: Any
    _top_name: str
    identity: str
    notification_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_identity_notification_topic")
    include_original_headers: Optional[bool] = None
    topic_arn: Optional[str] = None
