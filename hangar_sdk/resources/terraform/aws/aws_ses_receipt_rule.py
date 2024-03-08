from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AddHeaderAction(AbstractTerraformBlock):
    header_name: str
    header_value: str
    position: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="add_header_action")


@define(kw_only=True, slots=False)
class BounceAction(AbstractTerraformBlock):
    message: str
    position: int
    sender: str
    smtp_reply_code: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="bounce_action")
    status_code: Optional[str] = None
    topic_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class LambdaAction(AbstractTerraformBlock):
    function_arn: str
    position: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="lambda_action")
    invocation_type: Optional[str] = None
    topic_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class S3Action(AbstractTerraformBlock):
    bucket_name: str
    position: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_action")
    kms_key_arn: Optional[str] = None
    object_key_prefix: Optional[str] = None
    topic_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class SnsAction(AbstractTerraformBlock):
    position: int
    topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sns_action")
    encoding: Optional[str] = None


@define(kw_only=True, slots=False)
class StopAction(AbstractTerraformBlock):
    position: int
    scope: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="stop_action")
    topic_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class WorkmailAction(AbstractTerraformBlock):
    organization_arn: str
    position: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="workmail_action")
    topic_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesReceiptRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    rule_set_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_receipt_rule")
    add_header_action: Optional[Sequence[AddHeaderAction]] = None
    after: Optional[str] = None
    bounce_action: Optional[Sequence[BounceAction]] = None
    enabled: Optional[bool] = None
    lambda_action: Optional[Sequence[LambdaAction]] = None
    recipients: Optional[Sequence[str]] = None
    s3_action: Optional[Sequence[S3Action]] = None
    scan_enabled: Optional[bool] = None
    sns_action: Optional[Sequence[SnsAction]] = None
    stop_action: Optional[Sequence[StopAction]] = None
    tls_policy: Optional[str] = None
    workmail_action: Optional[Sequence[WorkmailAction]] = None
