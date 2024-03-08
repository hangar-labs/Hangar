from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDocdbClusterSnapshot(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_cluster_identifier: str
    db_cluster_snapshot_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdb_cluster_snapshot")
    timeouts: Optional[Timeouts] = None
