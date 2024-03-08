from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Location(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="location")
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3DirectoryBucket(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_directory_bucket")
    data_redundancy: Optional[str] = None
    force_destroy: Optional[bool] = None
    location: Optional[Sequence[Location]] = None
    type: Optional[str] = None
