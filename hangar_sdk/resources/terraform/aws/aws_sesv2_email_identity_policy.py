from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSesv2EmailIdentityPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    email_identity: str
    policy: str
    policy_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sesv2_email_identity_policy")
