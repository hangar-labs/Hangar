from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSesv2EmailIdentityFeedbackAttributes(AbstractTerraformResource):
    _group: Any
    _top_name: str
    email_identity: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_sesv2_email_identity_feedback_attributes"
    )
    email_forwarding_enabled: Optional[bool] = None
