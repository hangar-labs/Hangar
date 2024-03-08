from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class BlueGreenUpdate(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="blue_green_update")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class RestoreToPointInTime(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="restore_to_point_in_time")
    restore_time: Optional[str] = None
    source_db_instance_automated_backups_arn: Optional[str] = None
    source_db_instance_identifier: Optional[str] = None
    source_dbi_resource_id: Optional[str] = None
    use_latest_restorable_time: Optional[bool] = None


@define(kw_only=True, slots=False)
class S3Import(AbstractTerraformBlock):
    bucket_name: str
    ingestion_role: str
    source_engine: str
    source_engine_version: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_import")
    bucket_prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    instance_class: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_instance")
    allocated_storage: Optional[int] = None
    allow_major_version_upgrade: Optional[bool] = None
    apply_immediately: Optional[bool] = None
    auto_minor_version_upgrade: Optional[bool] = None
    availability_zone: Optional[str] = None
    backup_retention_period: Optional[int] = None
    backup_target: Optional[str] = None
    backup_window: Optional[str] = None
    blue_green_update: Optional[Sequence[BlueGreenUpdate]] = None
    ca_cert_identifier: Optional[str] = None
    character_set_name: Optional[str] = None
    copy_tags_to_snapshot: Optional[bool] = None
    custom_iam_instance_profile: Optional[str] = None
    customer_owned_ip_enabled: Optional[bool] = None
    db_name: Optional[str] = None
    db_subnet_group_name: Optional[str] = None
    delete_automated_backups: Optional[bool] = None
    deletion_protection: Optional[bool] = None
    domain: Optional[str] = None
    domain_auth_secret_arn: Optional[str] = None
    domain_dns_ips: Optional[Sequence[str]] = None
    domain_fqdn: Optional[str] = None
    domain_iam_role_name: Optional[str] = None
    domain_ou: Optional[str] = None
    enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    final_snapshot_identifier: Optional[str] = None
    iam_database_authentication_enabled: Optional[bool] = None
    identifier: Optional[str] = None
    identifier_prefix: Optional[str] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    license_model: Optional[str] = None
    maintenance_window: Optional[str] = None
    manage_master_user_password: Optional[bool] = None
    master_user_secret_kms_key_id: Optional[str] = None
    max_allocated_storage: Optional[int] = None
    monitoring_interval: Optional[int] = None
    monitoring_role_arn: Optional[str] = None
    multi_az: Optional[bool] = None
    nchar_character_set_name: Optional[str] = None
    network_type: Optional[str] = None
    option_group_name: Optional[str] = None
    parameter_group_name: Optional[str] = None
    password: Optional[str] = None
    performance_insights_enabled: Optional[bool] = None
    performance_insights_kms_key_id: Optional[str] = None
    performance_insights_retention_period: Optional[int] = None
    port: Optional[int] = None
    publicly_accessible: Optional[bool] = None
    replica_mode: Optional[str] = None
    replicate_source_db: Optional[str] = None
    restore_to_point_in_time: Optional[Sequence[RestoreToPointInTime]] = None
    s3_import: Optional[Sequence[S3Import]] = None
    skip_final_snapshot: Optional[bool] = None
    snapshot_identifier: Optional[str] = None
    storage_encrypted: Optional[bool] = None
    storage_throughput: Optional[int] = None
    storage_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    timezone: Optional[str] = None
    username: Optional[str] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
