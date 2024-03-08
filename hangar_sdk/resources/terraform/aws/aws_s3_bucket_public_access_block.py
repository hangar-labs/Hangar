from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3BucketPublicAccessBlock(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_public_access_block")
    block_public_acls: Optional[bool] = None
    block_public_policy: Optional[bool] = None
    ignore_public_acls: Optional[bool] = None
    restrict_public_buckets: Optional[bool] = None
