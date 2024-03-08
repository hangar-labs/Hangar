from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class VersioningConfiguration(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="versioning_configuration")
    mfa_delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3BucketVersioning(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_versioning")
    expected_bucket_owner: Optional[str] = None
    mfa: Optional[str] = None
    versioning_configuration: Optional[Sequence[VersioningConfiguration]] = None
