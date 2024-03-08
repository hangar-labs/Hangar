from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RestoreToPointInTime(AbstractTerraformBlock):
    source_cluster_identifier: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="restore_to_point_in_time")
    restore_to_time: Optional[str] = None
    restore_type: Optional[str] = None
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
class ScalingConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scaling_configuration")
    auto_pause: Optional[bool] = None
    max_capacity: Optional[int] = None
    min_capacity: Optional[int] = None
    seconds_until_auto_pause: Optional[int] = None
    timeout_action: Optional[str] = None


@define(kw_only=True, slots=False)
class Serverlessv2ScalingConfiguration(AbstractTerraformBlock):
    max_capacity: int
    min_capacity: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="serverlessv2_scaling_configuration")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRdsCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    engine: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_cluster")
    allocated_storage: Optional[int] = None
    allow_major_version_upgrade: Optional[bool] = None
    apply_immediately: Optional[bool] = None
    availability_zones: Optional[Sequence[str]] = None
    backtrack_window: Optional[int] = None
    backup_retention_period: Optional[int] = None
    cluster_identifier: Optional[str] = None
    cluster_identifier_prefix: Optional[str] = None
    cluster_members: Optional[Sequence[str]] = None
    copy_tags_to_snapshot: Optional[bool] = None
    database_name: Optional[str] = None
    db_cluster_instance_class: Optional[str] = None
    db_cluster_parameter_group_name: Optional[str] = None
    db_instance_parameter_group_name: Optional[str] = None
    db_subnet_group_name: Optional[str] = None
    db_system_id: Optional[str] = None
    delete_automated_backups: Optional[bool] = None
    deletion_protection: Optional[bool] = None
    domain: Optional[str] = None
    domain_iam_role_name: Optional[str] = None
    enable_global_write_forwarding: Optional[bool] = None
    enable_http_endpoint: Optional[bool] = None
    enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None
    engine_mode: Optional[str] = None
    engine_version: Optional[str] = None
    final_snapshot_identifier: Optional[str] = None
    global_cluster_identifier: Optional[str] = None
    iam_database_authentication_enabled: Optional[bool] = None
    iam_roles: Optional[Sequence[str]] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    manage_master_user_password: Optional[bool] = None
    master_password: Optional[str] = None
    master_user_secret_kms_key_id: Optional[str] = None
    master_username: Optional[str] = None
    network_type: Optional[str] = None
    port: Optional[int] = None
    preferred_backup_window: Optional[str] = None
    preferred_maintenance_window: Optional[str] = None
    replication_source_identifier: Optional[str] = None
    restore_to_point_in_time: Optional[Sequence[RestoreToPointInTime]] = None
    s3_import: Optional[Sequence[S3Import]] = None
    scaling_configuration: Optional[Sequence[ScalingConfiguration]] = None
    serverlessv2_scaling_configuration: Optional[
        Sequence[Serverlessv2ScalingConfiguration]
    ] = None
    skip_final_snapshot: Optional[bool] = None
    snapshot_identifier: Optional[str] = None
    source_region: Optional[str] = None
    storage_encrypted: Optional[bool] = None
    storage_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
