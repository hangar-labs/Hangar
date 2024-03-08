from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Grantee(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grantee")
    email_address: Optional[str] = None
    uri: Optional[str] = None


@define(kw_only=True, slots=False)
class Grant(AbstractTerraformBlock):
    permission: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grant")
    grantee: Optional[Sequence[Grantee]] = None


@define(kw_only=True, slots=False)
class Owner(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="owner")
    display_name: Optional[str] = None


@define(kw_only=True, slots=False)
class AccessControlPolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_control_policy")
    grant: Optional[Sequence[Grant]] = None
    owner: Optional[Sequence[Owner]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketAcl(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_acl")
    access_control_policy: Optional[Sequence[AccessControlPolicy]] = None
    acl: Optional[str] = None
    expected_bucket_owner: Optional[str] = None
