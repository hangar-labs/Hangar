from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsWorklinkWebsiteCertificateAuthorityAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    certificate: str
    fleet_arn: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_worklink_website_certificate_authority_association"
    )
    display_name: Optional[str] = None
