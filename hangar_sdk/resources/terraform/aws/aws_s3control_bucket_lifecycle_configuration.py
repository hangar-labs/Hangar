from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AbortIncompleteMultipartUpload(AbstractTerraformBlock):
    days_after_initiation: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="abort_incomplete_multipart_upload")


@define(kw_only=True, slots=False)
class Expiration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="expiration")
    date: Optional[str] = None
    days: Optional[int] = None
    expired_object_delete_marker: Optional[bool] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    abort_incomplete_multipart_upload: Optional[
        Sequence[AbortIncompleteMultipartUpload]
    ] = None
    expiration: Optional[Sequence[Expiration]] = None
    filter: Optional[Sequence[Filter]] = None
    status: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3controlBucketLifecycleConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3control_bucket_lifecycle_configuration"
    )
    rule: Optional[Sequence[Rule]] = None
