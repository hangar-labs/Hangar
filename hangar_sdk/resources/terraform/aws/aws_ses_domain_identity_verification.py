from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesDomainIdentityVerification(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_domain_identity_verification")
    timeouts: Optional[Timeouts] = None
