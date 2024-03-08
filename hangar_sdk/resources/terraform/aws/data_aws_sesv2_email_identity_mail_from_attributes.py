from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSesv2EmailIdentityMailFromAttributes(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    email_identity: str
    _block_type: str = "datasource"
    _name: str = field(
        alias="_name", default="aws_sesv2_email_identity_mail_from_attributes"
    )
