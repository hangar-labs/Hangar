from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSqsQueue(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sqs_queue")
    content_based_deduplication: Optional[bool] = None
    deduplication_scope: Optional[str] = None
    delay_seconds: Optional[int] = None
    fifo_queue: Optional[bool] = None
    fifo_throughput_limit: Optional[str] = None
    kms_data_key_reuse_period_seconds: Optional[int] = None
    kms_master_key_id: Optional[str] = None
    max_message_size: Optional[int] = None
    message_retention_seconds: Optional[int] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    policy: Optional[str] = None
    receive_wait_time_seconds: Optional[int] = None
    redrive_allow_policy: Optional[str] = None
    redrive_policy: Optional[str] = None
    sqs_managed_sse_enabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    visibility_timeout_seconds: Optional[int] = None
