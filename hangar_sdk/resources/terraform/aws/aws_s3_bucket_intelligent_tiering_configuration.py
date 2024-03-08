from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class Tiering(AbstractTerraformBlock):
    access_tier: str
    days: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tiering")


@define(kw_only=True, slots=False)
class AwsS3BucketIntelligentTieringConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3_bucket_intelligent_tiering_configuration"
    )
    filter: Optional[Sequence[Filter]] = None
    status: Optional[str] = None
    tiering: Optional[Sequence[Tiering]] = None
