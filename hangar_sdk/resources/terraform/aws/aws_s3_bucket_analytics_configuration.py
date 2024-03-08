from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class S3BucketDestination(AbstractTerraformBlock):
    bucket_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_bucket_destination")
    bucket_account_id: Optional[str] = None
    format: Optional[str] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")
    s3_bucket_destination: Optional[Sequence[S3BucketDestination]] = None


@define(kw_only=True, slots=False)
class DataExport(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="data_export")
    destination: Optional[Sequence[Destination]] = None
    output_schema_version: Optional[str] = None


@define(kw_only=True, slots=False)
class StorageClassAnalysis(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="storage_class_analysis")
    data_export: Optional[Sequence[DataExport]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketAnalyticsConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_analytics_configuration")
    filter: Optional[Sequence[Filter]] = None
    storage_class_analysis: Optional[Sequence[StorageClassAnalysis]] = None
