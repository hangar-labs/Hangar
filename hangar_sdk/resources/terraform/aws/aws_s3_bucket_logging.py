from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Grantee(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grantee")
    email_address: Optional[str] = None
    uri: Optional[str] = None


@define(kw_only=True, slots=False)
class TargetGrant(AbstractTerraformBlock):
    permission: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_grant")
    grantee: Optional[Sequence[Grantee]] = None


@define(kw_only=True, slots=False)
class PartitionedPrefix(AbstractTerraformBlock):
    partition_date_source: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="partitioned_prefix")


@define(kw_only=True, slots=False)
class SimplePrefix(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="simple_prefix")


@define(kw_only=True, slots=False)
class TargetObjectKeyFormat(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_object_key_format")
    partitioned_prefix: Optional[Sequence[PartitionedPrefix]] = None
    simple_prefix: Optional[Sequence[SimplePrefix]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketLogging(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    target_bucket: str
    target_prefix: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_logging")
    expected_bucket_owner: Optional[str] = None
    target_grant: Optional[Sequence[TargetGrant]] = None
    target_object_key_format: Optional[Sequence[TargetObjectKeyFormat]] = None
