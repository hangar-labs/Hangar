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
class AwsEbsSnapshot(AbstractTerraformResource):
    _group: Any
    _top_name: str
    volume_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ebs_snapshot")
    description: Optional[str] = None
    outpost_arn: Optional[str] = None
    permanent_restore: Optional[bool] = None
    storage_tier: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    temporary_restore_days: Optional[int] = None
    timeouts: Optional[Timeouts] = None
