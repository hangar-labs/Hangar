from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDmsS3Endpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket_name: str
    endpoint_id: str
    endpoint_type: str
    service_access_role_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dms_s3_endpoint")
    add_column_name: Optional[bool] = None
    add_trailing_padding_character: Optional[bool] = None
    bucket_folder: Optional[str] = None
    canned_acl_for_objects: Optional[str] = None
    cdc_inserts_and_updates: Optional[bool] = None
    cdc_inserts_only: Optional[bool] = None
    cdc_max_batch_interval: Optional[int] = None
    cdc_min_file_size: Optional[int] = None
    cdc_path: Optional[str] = None
    certificate_arn: Optional[str] = None
    compression_type: Optional[str] = None
    csv_delimiter: Optional[str] = None
    csv_no_sup_value: Optional[str] = None
    csv_null_value: Optional[str] = None
    csv_row_delimiter: Optional[str] = None
    data_format: Optional[str] = None
    data_page_size: Optional[int] = None
    date_partition_delimiter: Optional[str] = None
    date_partition_enabled: Optional[bool] = None
    date_partition_sequence: Optional[str] = None
    date_partition_timezone: Optional[str] = None
    detach_target_on_lob_lookup_failure_parquet: Optional[bool] = None
    dict_page_size_limit: Optional[int] = None
    enable_statistics: Optional[bool] = None
    encoding_type: Optional[str] = None
    encryption_mode: Optional[str] = None
    expected_bucket_owner: Optional[str] = None
    external_table_definition: Optional[str] = None
    glue_catalog_generation: Optional[bool] = None
    ignore_header_rows: Optional[int] = None
    include_op_for_full_load: Optional[bool] = None
    kms_key_arn: Optional[str] = None
    max_file_size: Optional[int] = None
    parquet_timestamp_in_millisecond: Optional[bool] = None
    parquet_version: Optional[str] = None
    preserve_transactions: Optional[bool] = None
    rfc_4180: Optional[bool] = None
    row_group_length: Optional[int] = None
    server_side_encryption_kms_key_id: Optional[str] = None
    ssl_mode: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    timestamp_column_name: Optional[str] = None
    use_csv_no_sup_value: Optional[bool] = None
    use_task_start_time_for_full_load_timestamp: Optional[bool] = None
