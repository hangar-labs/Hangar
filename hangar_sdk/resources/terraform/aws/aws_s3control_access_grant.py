from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AccessGrantsLocationConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_grants_location_configuration")
    s3_sub_prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class Grantee(AbstractTerraformBlock):
    grantee_identifier: str
    grantee_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grantee")


@define(kw_only=True, slots=False)
class AwsS3controlAccessGrant(AbstractTerraformResource):
    _group: Any
    _top_name: str
    access_grants_location_id: str
    permission: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3control_access_grant")
    access_grants_location_configuration: Optional[
        Sequence[AccessGrantsLocationConfiguration]
    ] = None
    account_id: Optional[str] = None
    grantee: Optional[Sequence[Grantee]] = None
    s3_prefix_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
