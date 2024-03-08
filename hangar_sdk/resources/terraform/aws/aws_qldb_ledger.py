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
class AwsQldbLedger(AbstractTerraformResource):
    _group: Any
    _top_name: str
    permissions_mode: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_qldb_ledger")
    deletion_protection: Optional[bool] = None
    kms_key: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
