from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ActivityMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="activity_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AdvancedCostOptimizationMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="advanced_cost_optimization_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AdvancedDataProtectionMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="advanced_data_protection_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class ActivityMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="activity_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AdvancedCostOptimizationMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="advanced_cost_optimization_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AdvancedDataProtectionMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="advanced_data_protection_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class DetailedStatusCodeMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="detailed_status_code_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class SelectionCriteria(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="selection_criteria")
    delimiter: Optional[str] = None
    max_depth: Optional[int] = None
    min_storage_bytes_percentage: Optional[int] = None


@define(kw_only=True, slots=False)
class StorageMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="storage_metrics")
    enabled: Optional[bool] = None
    selection_criteria: Optional[Sequence[SelectionCriteria]] = None


@define(kw_only=True, slots=False)
class PrefixLevel(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="prefix_level")
    storage_metrics: Optional[Sequence[StorageMetrics]] = None


@define(kw_only=True, slots=False)
class BucketLevel(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="bucket_level")
    activity_metrics: Optional[Sequence[ActivityMetrics]] = None
    advanced_cost_optimization_metrics: Optional[
        Sequence[AdvancedCostOptimizationMetrics]
    ] = None
    advanced_data_protection_metrics: Optional[
        Sequence[AdvancedDataProtectionMetrics]
    ] = None
    detailed_status_code_metrics: Optional[Sequence[DetailedStatusCodeMetrics]] = None
    prefix_level: Optional[Sequence[PrefixLevel]] = None


@define(kw_only=True, slots=False)
class DetailedStatusCodeMetrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="detailed_status_code_metrics")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AccountLevel(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="account_level")
    activity_metrics: Optional[Sequence[ActivityMetrics]] = None
    advanced_cost_optimization_metrics: Optional[
        Sequence[AdvancedCostOptimizationMetrics]
    ] = None
    advanced_data_protection_metrics: Optional[
        Sequence[AdvancedDataProtectionMetrics]
    ] = None
    bucket_level: Optional[Sequence[BucketLevel]] = None
    detailed_status_code_metrics: Optional[Sequence[DetailedStatusCodeMetrics]] = None


@define(kw_only=True, slots=False)
class AwsOrg(AbstractTerraformBlock):
    arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="aws_org")


@define(kw_only=True, slots=False)
class CloudWatchMetrics(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloud_watch_metrics")


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
class S3BucketDestination(AbstractTerraformBlock):
    account_id: str
    arn: str
    format: str
    output_schema_version: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_bucket_destination")
    encryption: Optional[Sequence[Encryption]] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class DataExport(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="data_export")
    cloud_watch_metrics: Optional[Sequence[CloudWatchMetrics]] = None
    s3_bucket_destination: Optional[Sequence[S3BucketDestination]] = None


@define(kw_only=True, slots=False)
class Exclude(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="exclude")
    buckets: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Include(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="include")
    buckets: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class StorageLensConfiguration(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="storage_lens_configuration")
    account_level: Optional[Sequence[AccountLevel]] = None
    aws_org: Optional[Sequence[AwsOrg]] = None
    data_export: Optional[Sequence[DataExport]] = None
    exclude: Optional[Sequence[Exclude]] = None
    include: Optional[Sequence[Include]] = None


@define(kw_only=True, slots=False)
class AwsS3controlStorageLensConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    config_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3control_storage_lens_configuration"
    )
    account_id: Optional[str] = None
    storage_lens_configuration: Optional[Sequence[StorageLensConfiguration]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
