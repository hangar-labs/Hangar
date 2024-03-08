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
class AwsRdsCustomDbEngineVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    engine: str
    engine_version: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_custom_db_engine_version")
    database_installation_files_s3_bucket_name: Optional[str] = None
    database_installation_files_s3_prefix: Optional[str] = None
    description: Optional[str] = None
    filename: Optional[str] = None
    kms_key_id: Optional[str] = None
    manifest: Optional[str] = None
    manifest_hash: Optional[str] = None
    source_image_id: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
