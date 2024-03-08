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
class AwsMemorydbCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    acl_name: str
    node_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_memorydb_cluster")
    auto_minor_version_upgrade: Optional[bool] = None
    data_tiering: Optional[bool] = None
    description: Optional[str] = None
    engine_version: Optional[str] = None
    final_snapshot_name: Optional[str] = None
    kms_key_arn: Optional[str] = None
    maintenance_window: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    num_replicas_per_shard: Optional[int] = None
    num_shards: Optional[int] = None
    parameter_group_name: Optional[str] = None
    port: Optional[int] = None
    security_group_ids: Optional[Sequence[str]] = None
    snapshot_arns: Optional[Sequence[str]] = None
    snapshot_name: Optional[str] = None
    snapshot_retention_limit: Optional[int] = None
    snapshot_window: Optional[str] = None
    sns_topic_arn: Optional[str] = None
    subnet_group_name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    tls_enabled: Optional[bool] = None
