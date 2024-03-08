from typing import Any, Dict, Optional

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
class AwsDocdbClusterInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_identifier: str
    instance_class: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdb_cluster_instance")
    apply_immediately: Optional[bool] = None
    auto_minor_version_upgrade: Optional[bool] = None
    availability_zone: Optional[str] = None
    ca_cert_identifier: Optional[str] = None
    copy_tags_to_snapshot: Optional[bool] = None
    enable_performance_insights: Optional[bool] = None
    engine: Optional[str] = None
    identifier: Optional[str] = None
    identifier_prefix: Optional[str] = None
    performance_insights_kms_key_id: Optional[str] = None
    preferred_maintenance_window: Optional[str] = None
    promotion_tier: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
