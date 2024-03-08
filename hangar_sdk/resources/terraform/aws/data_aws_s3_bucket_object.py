from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsS3BucketObject(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    bucket: str
    key: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_s3_bucket_object")
    range: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    version_id: Optional[str] = None
