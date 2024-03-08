from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class SseKms(AbstractTerraformBlock):
    key_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sse_kms")


@define(kw_only=True, slots=False)
class SseS3(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sse_s3")


@define(kw_only=True, slots=False)
class Encryption(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="encryption")
    sse_kms: Optional[Sequence[SseKms]] = None
    sse_s3: Optional[Sequence[SseS3]] = None


@define(kw_only=True, slots=False)
class Bucket(AbstractTerraformBlock):
    bucket_arn: str
    format: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="bucket")
    account_id: Optional[str] = None
    encryption: Optional[Sequence[Encryption]] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")
    bucket: Optional[Sequence[Bucket]] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class Schedule(AbstractTerraformBlock):
    frequency: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="schedule")


@define(kw_only=True, slots=False)
class AwsS3BucketInventory(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    included_object_versions: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_inventory")
    destination: Optional[Sequence[Destination]] = None
    enabled: Optional[bool] = None
    filter: Optional[Sequence[Filter]] = None
    optional_fields: Optional[Sequence[str]] = None
    schedule: Optional[Sequence[Schedule]] = None
