from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamSecurityTokenServicePreferences(AbstractTerraformResource):
    _group: Any
    _top_name: str
    global_endpoint_token_version: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_iam_security_token_service_preferences"
    )
