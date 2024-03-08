from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    access_point: Optional[str] = None
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketMetric(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_metric")
    filter: Optional[Sequence[Filter]] = None
