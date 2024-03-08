from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class LambdaFunction(AbstractTerraformBlock):
    events: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="lambda_function")
    filter_prefix: Optional[str] = None
    filter_suffix: Optional[str] = None
    lambda_function_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Queue(AbstractTerraformBlock):
    events: Sequence[str]
    queue_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="queue")
    filter_prefix: Optional[str] = None
    filter_suffix: Optional[str] = None


@define(kw_only=True, slots=False)
class Topic(AbstractTerraformBlock):
    events: Sequence[str]
    topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="topic")
    filter_prefix: Optional[str] = None
    filter_suffix: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3BucketNotification(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_notification")
    eventbridge: Optional[bool] = None
    lambda_function: Optional[Sequence[LambdaFunction]] = None
    queue: Optional[Sequence[Queue]] = None
    topic: Optional[Sequence[Topic]] = None
