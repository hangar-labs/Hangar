from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbSnapshot(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_instance_identifier: str
    db_snapshot_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_snapshot")
    shared_accounts: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
