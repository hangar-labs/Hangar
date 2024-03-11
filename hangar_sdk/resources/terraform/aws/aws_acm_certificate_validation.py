from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Optional,Sequence


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsAcmCertificateValidation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    certificate_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_acm_certificate_validation")
    timeouts: Optional[Timeouts] = None
    validation_record_fqdns: Optional[Sequence[str]] = None