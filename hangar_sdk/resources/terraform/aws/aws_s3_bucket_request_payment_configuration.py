from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3BucketRequestPaymentConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    payer: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3_bucket_request_payment_configuration"
    )
    expected_bucket_owner: Optional[str] = None
