from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsS3BucketObjects(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_s3_bucket_objects")
    delimiter: Optional[str] = None
    encoding_type: Optional[str] = None
    fetch_owner: Optional[bool] = None
    max_keys: Optional[int] = None
    prefix: Optional[str] = None
    start_after: Optional[str] = None
