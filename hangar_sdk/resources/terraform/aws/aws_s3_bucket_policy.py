from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3BucketPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_policy")
