from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSesDomainMailFrom(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain: str
    mail_from_domain: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_domain_mail_from")
    behavior_on_mx_failure: Optional[str] = None
