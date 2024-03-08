from typing import Any, Optional

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
class AwsDocdbGlobalCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    global_cluster_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdb_global_cluster")
    database_name: Optional[str] = None
    deletion_protection: Optional[bool] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    source_db_cluster_identifier: Optional[str] = None
    storage_encrypted: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
