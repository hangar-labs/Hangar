from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRdsOrderableDbInstance(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    engine: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_rds_orderable_db_instance")
    availability_zone_group: Optional[str] = None
    engine_latest_version: Optional[bool] = None
    engine_version: Optional[str] = None
    instance_class: Optional[str] = None
    license_model: Optional[str] = None
    preferred_engine_versions: Optional[Sequence[str]] = None
    preferred_instance_classes: Optional[Sequence[str]] = None
    read_replica_capable: Optional[bool] = None
    storage_type: Optional[str] = None
    supported_engine_modes: Optional[Sequence[str]] = None
    supported_network_types: Optional[Sequence[str]] = None
    supports_clusters: Optional[bool] = None
    supports_enhanced_monitoring: Optional[bool] = None
    supports_global_databases: Optional[bool] = None
    supports_iam_database_authentication: Optional[bool] = None
    supports_iops: Optional[bool] = None
    supports_kerberos_authentication: Optional[bool] = None
    supports_multi_az: Optional[bool] = None
    supports_performance_insights: Optional[bool] = None
    supports_storage_autoscaling: Optional[bool] = None
    supports_storage_encryption: Optional[bool] = None
    vpc: Optional[bool] = None
