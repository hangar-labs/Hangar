from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AbortIncompleteMultipartUpload(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="abort_incomplete_multipart_upload")
    days_after_initiation: Optional[int] = None


@define(kw_only=True, slots=False)
class Expiration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="expiration")
    date: Optional[str] = None
    days: Optional[int] = None
    expired_object_delete_marker: Optional[bool] = None


@define(kw_only=True, slots=False)
class Tag(AbstractTerraformBlock):
    key: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag")


@define(kw_only=True, slots=False)
class TerraformAnd(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="terraform_and")
    object_size_greater_than: Optional[int] = None
    object_size_less_than: Optional[int] = None
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    object_size_greater_than: Optional[str] = None
    object_size_less_than: Optional[str] = None
    prefix: Optional[str] = None
    tag: Optional[Sequence[Tag]] = None
    terraform_and: Optional[Sequence[TerraformAnd]] = None


@define(kw_only=True, slots=False)
class NoncurrentVersionExpiration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="noncurrent_version_expiration")
    newer_noncurrent_versions: Optional[str] = None
    noncurrent_days: Optional[int] = None


@define(kw_only=True, slots=False)
class NoncurrentVersionTransition(AbstractTerraformBlock):
    storage_class: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="noncurrent_version_transition")
    newer_noncurrent_versions: Optional[str] = None
    noncurrent_days: Optional[int] = None


@define(kw_only=True, slots=False)
class Transition(AbstractTerraformBlock):
    storage_class: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="transition")
    date: Optional[str] = None
    days: Optional[int] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    abort_incomplete_multipart_upload: Optional[
        Sequence[AbortIncompleteMultipartUpload]
    ] = None
    expiration: Optional[Sequence[Expiration]] = None
    filter: Optional[Sequence[Filter]] = None
    noncurrent_version_expiration: Optional[Sequence[NoncurrentVersionExpiration]] = (
        None
    )
    noncurrent_version_transition: Optional[Sequence[NoncurrentVersionTransition]] = (
        None
    )
    prefix: Optional[str] = None
    transition: Optional[Sequence[Transition]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3BucketLifecycleConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_lifecycle_configuration")
    expected_bucket_owner: Optional[str] = None
    rule: Optional[Sequence[Rule]] = None
    timeouts: Optional[Timeouts] = None
