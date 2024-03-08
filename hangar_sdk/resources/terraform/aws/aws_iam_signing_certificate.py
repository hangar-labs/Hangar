from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamSigningCertificate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    certificate_body: str
    user_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_signing_certificate")
    status: Optional[str] = None
