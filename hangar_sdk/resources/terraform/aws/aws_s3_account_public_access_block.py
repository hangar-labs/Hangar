from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3AccountPublicAccessBlock(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_account_public_access_block")
    account_id: Optional[str] = None
    block_public_acls: Optional[bool] = None
    block_public_policy: Optional[bool] = None
    ignore_public_acls: Optional[bool] = None
    restrict_public_buckets: Optional[bool] = None
