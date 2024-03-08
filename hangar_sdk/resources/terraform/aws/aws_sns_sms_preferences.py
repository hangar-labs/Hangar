from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSnsSmsPreferences(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sns_sms_preferences")
    default_sender_id: Optional[str] = None
    default_sms_type: Optional[str] = None
    delivery_status_iam_role_arn: Optional[str] = None
    delivery_status_success_sampling_rate: Optional[str] = None
    monthly_spend_limit: Optional[int] = None
    usage_report_s3_bucket: Optional[str] = None
