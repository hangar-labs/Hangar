from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PublicAccessBlockConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="public_access_block_configuration")
    block_public_acls: Optional[bool] = None
    block_public_policy: Optional[bool] = None
    ignore_public_acls: Optional[bool] = None
    restrict_public_buckets: Optional[bool] = None


@define(kw_only=True, slots=False)
class VpcConfiguration(AbstractTerraformBlock):
    vpc_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vpc_configuration")


@define(kw_only=True, slots=False)
class AwsS3AccessPoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_access_point")
    account_id: Optional[str] = None
    bucket_account_id: Optional[str] = None
    policy: Optional[str] = None
    public_access_block_configuration: Optional[
        Sequence[PublicAccessBlockConfiguration]
    ] = None
    vpc_configuration: Optional[Sequence[VpcConfiguration]] = None
