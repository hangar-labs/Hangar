from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ClientData(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="client_data")
    comment: Optional[str] = None
    upload_end: Optional[str] = None
    upload_size: Optional[int] = None
    upload_start: Optional[str] = None


@define(kw_only=True, slots=False)
class UserBucket(AbstractTerraformBlock):
    s3_bucket: str
    s3_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="user_bucket")


@define(kw_only=True, slots=False)
class DiskContainer(AbstractTerraformBlock):
    format: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="disk_container")
    description: Optional[str] = None
    url: Optional[str] = None
    user_bucket: Optional[Sequence[UserBucket]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEbsSnapshotImport(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ebs_snapshot_import")
    client_data: Optional[Sequence[ClientData]] = None
    description: Optional[str] = None
    disk_container: Optional[Sequence[DiskContainer]] = None
    encrypted: Optional[bool] = None
    kms_key_id: Optional[str] = None
    permanent_restore: Optional[bool] = None
    role_name: Optional[str] = None
    storage_tier: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    temporary_restore_days: Optional[int] = None
    timeouts: Optional[Timeouts] = None
