from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDocdbCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdb_cluster")
    allow_major_version_upgrade: Optional[bool] = None
    apply_immediately: Optional[bool] = None
    availability_zones: Optional[Sequence[str]] = None
    backup_retention_period: Optional[int] = None
    cluster_identifier: Optional[str] = None
    cluster_identifier_prefix: Optional[str] = None
    cluster_members: Optional[Sequence[str]] = None
    db_cluster_parameter_group_name: Optional[str] = None
    db_subnet_group_name: Optional[str] = None
    deletion_protection: Optional[bool] = None
    enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    final_snapshot_identifier: Optional[str] = None
    global_cluster_identifier: Optional[str] = None
    kms_key_id: Optional[str] = None
    master_password: Optional[str] = None
    master_username: Optional[str] = None
    port: Optional[int] = None
    preferred_backup_window: Optional[str] = None
    preferred_maintenance_window: Optional[str] = None
    skip_final_snapshot: Optional[bool] = None
    snapshot_identifier: Optional[str] = None
    storage_encrypted: Optional[bool] = None
    storage_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
