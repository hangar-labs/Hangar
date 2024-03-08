from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class S3Config(AbstractTerraformBlock):
    bucket_access_role_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_config")


@define(kw_only=True, slots=False)
class AwsDatasyncLocationS3(AbstractTerraformResource):
    _group: Any
    _top_name: str
    s3_bucket_arn: str
    subdirectory: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_datasync_location_s3")
    agent_arns: Optional[Sequence[str]] = None
    s3_config: Optional[Sequence[S3Config]] = None
    s3_storage_class: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
