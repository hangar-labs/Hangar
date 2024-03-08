from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    object_ownership: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")


@define(kw_only=True, slots=False)
class AwsS3BucketOwnershipControls(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_ownership_controls")
    rule: Optional[Sequence[Rule]] = None
