from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CorsRule(AbstractTerraformBlock):
    allowed_methods: Sequence[str]
    allowed_origins: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cors_rule")
    allowed_headers: Optional[Sequence[str]] = None
    expose_headers: Optional[Sequence[str]] = None
    max_age_seconds: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsS3BucketCorsConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_cors_configuration")
    cors_rule: Optional[Sequence[CorsRule]] = None
    expected_bucket_owner: Optional[str] = None
