from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3controlBucket(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    outpost_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3control_bucket")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
