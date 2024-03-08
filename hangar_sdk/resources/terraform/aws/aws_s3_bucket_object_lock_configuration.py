from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DefaultRetention(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_retention")
    days: Optional[int] = None
    mode: Optional[str] = None
    years: Optional[int] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    default_retention: Optional[Sequence[DefaultRetention]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketObjectLockConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_object_lock_configuration")
    expected_bucket_owner: Optional[str] = None
    object_lock_enabled: Optional[str] = None
    rule: Optional[Sequence[Rule]] = None
    token: Optional[str] = None
