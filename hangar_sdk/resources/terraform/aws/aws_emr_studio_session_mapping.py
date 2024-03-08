from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEmrStudioSessionMapping(AbstractTerraformResource):
    _group: Any
    _top_name: str
    identity_type: str
    session_policy_arn: str
    studio_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_emr_studio_session_mapping")
    identity_id: Optional[str] = None
    identity_name: Optional[str] = None
