from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsS3Object(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    bucket: str
    key: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_s3_object")
    checksum_mode: Optional[str] = None
    range: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    version_id: Optional[str] = None
