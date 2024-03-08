from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Attribute(AbstractTerraformBlock):
    name: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="attribute")


@define(kw_only=True, slots=False)
class GlobalSecondaryIndex(AbstractTerraformBlock):
    hash_key: str
    name: str
    projection_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="global_secondary_index")
    non_key_attributes: Optional[Sequence[str]] = None
    range_key: Optional[str] = None
    read_capacity: Optional[int] = None
    write_capacity: Optional[int] = None


@define(kw_only=True, slots=False)
class Csv(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="csv")
    delimiter: Optional[str] = None
    header_list: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class InputFormatOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="input_format_options")
    csv: Optional[Sequence[Csv]] = None


@define(kw_only=True, slots=False)
class S3BucketSource(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_bucket_source")
    bucket_owner: Optional[str] = None
    key_prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class ImportTable(AbstractTerraformBlock):
    input_format: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="import_table")
    input_compression_type: Optional[str] = None
    input_format_options: Optional[Sequence[InputFormatOptions]] = None
    s3_bucket_source: Optional[Sequence[S3BucketSource]] = None


@define(kw_only=True, slots=False)
class LocalSecondaryIndex(AbstractTerraformBlock):
    name: str
    projection_type: str
    range_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="local_secondary_index")
    non_key_attributes: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class PointInTimeRecovery(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="point_in_time_recovery")


@define(kw_only=True, slots=False)
class Replica(AbstractTerraformBlock):
    region_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replica")
    kms_key_arn: Optional[str] = None
    point_in_time_recovery: Optional[bool] = None
    propagate_tags: Optional[bool] = None


@define(kw_only=True, slots=False)
class ServerSideEncryption(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="server_side_encryption")
    kms_key_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class Ttl(AbstractTerraformBlock):
    attribute_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ttl")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AwsDynamodbTable(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dynamodb_table")
    attribute: Optional[Sequence[Attribute]] = None
    billing_mode: Optional[str] = None
    deletion_protection_enabled: Optional[bool] = None
    global_secondary_index: Optional[Sequence[GlobalSecondaryIndex]] = None
    hash_key: Optional[str] = None
    import_table: Optional[Sequence[ImportTable]] = None
    local_secondary_index: Optional[Sequence[LocalSecondaryIndex]] = None
    point_in_time_recovery: Optional[Sequence[PointInTimeRecovery]] = None
    range_key: Optional[str] = None
    read_capacity: Optional[int] = None
    replica: Optional[Sequence[Replica]] = None
    restore_date_time: Optional[str] = None
    restore_source_name: Optional[str] = None
    restore_to_latest_time: Optional[bool] = None
    server_side_encryption: Optional[Sequence[ServerSideEncryption]] = None
    stream_enabled: Optional[bool] = None
    stream_view_type: Optional[str] = None
    table_class: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    ttl: Optional[Sequence[Ttl]] = None
    write_capacity: Optional[int] = None
