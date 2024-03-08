from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbSnapshotCopy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    source_db_snapshot_identifier: str
    target_db_snapshot_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_snapshot_copy")
    copy_tags: Optional[bool] = None
    destination_region: Optional[str] = None
    kms_key_id: Optional[str] = None
    option_group_name: Optional[str] = None
    presigned_url: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_custom_availability_zone: Optional[str] = None
    timeouts: Optional[Timeouts] = None
