from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class S3Destination(AbstractTerraformBlock):
    bucket_name: str
    region: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_destination")
    kms_key_arn: Optional[str] = None
    prefix: Optional[str] = None
    sync_format: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSsmResourceDataSync(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_resource_data_sync")
    s3_destination: Optional[Sequence[S3Destination]] = None
