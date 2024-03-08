from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSnsPlatformApplication(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    platform: str
    platform_credential: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sns_platform_application")
    apple_platform_bundle_id: Optional[str] = None
    apple_platform_team_id: Optional[str] = None
    event_delivery_failure_topic_arn: Optional[str] = None
    event_endpoint_created_topic_arn: Optional[str] = None
    event_endpoint_deleted_topic_arn: Optional[str] = None
    event_endpoint_updated_topic_arn: Optional[str] = None
    failure_feedback_role_arn: Optional[str] = None
    platform_principal: Optional[str] = None
    success_feedback_role_arn: Optional[str] = None
    success_feedback_sample_rate: Optional[str] = None
