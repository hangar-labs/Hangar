from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSnsTopic(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sns_topic")
    application_failure_feedback_role_arn: Optional[str] = None
    application_success_feedback_role_arn: Optional[str] = None
    application_success_feedback_sample_rate: Optional[int] = None
    archive_policy: Optional[str] = None
    content_based_deduplication: Optional[bool] = None
    delivery_policy: Optional[str] = None
    display_name: Optional[str] = None
    fifo_topic: Optional[bool] = None
    firehose_failure_feedback_role_arn: Optional[str] = None
    firehose_success_feedback_role_arn: Optional[str] = None
    firehose_success_feedback_sample_rate: Optional[int] = None
    http_failure_feedback_role_arn: Optional[str] = None
    http_success_feedback_role_arn: Optional[str] = None
    http_success_feedback_sample_rate: Optional[int] = None
    kms_master_key_id: Optional[str] = None
    lambda_failure_feedback_role_arn: Optional[str] = None
    lambda_success_feedback_role_arn: Optional[str] = None
    lambda_success_feedback_sample_rate: Optional[int] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    policy: Optional[str] = None
    signature_version: Optional[int] = None
    sqs_failure_feedback_role_arn: Optional[str] = None
    sqs_success_feedback_role_arn: Optional[str] = None
    sqs_success_feedback_sample_rate: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tracing_config: Optional[str] = None
