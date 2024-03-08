from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3controlAccessGrantsLocation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    iam_role_arn: str
    location_scope: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3control_access_grants_location")
    account_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
