from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamServiceSpecificCredential(AbstractTerraformResource):
    _group: Any
    _top_name: str
    service_name: str
    user_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_service_specific_credential")
    status: Optional[str] = None
