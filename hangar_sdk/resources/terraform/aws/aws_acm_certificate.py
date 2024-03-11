from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Dict,Optional,Sequence


@define(kw_only=True, slots=False)
class Options(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="options")
    certificate_transparency_logging_preference: Optional[str] = None


@define(kw_only=True, slots=False)
class ValidationOption(AbstractTerraformBlock):
    domain_name: str
    validation_domain: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="validation_option")


@define(kw_only=True, slots=False)
class AwsAcmCertificate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_acm_certificate")
    certificate_authority_arn: Optional[str] = None
    certificate_body: Optional[str] = None
    certificate_chain: Optional[str] = None
    domain_name: Optional[str] = None
    early_renewal_duration: Optional[str] = None
    key_algorithm: Optional[str] = None
    options: Optional[Sequence[Options]] = None
    private_key: Optional[str] = None
    subject_alternative_names: Optional[Sequence[str]] = None
    tags: Optional[Dict[str,str]] = None
    tags_all: Optional[Dict[str,str]] = None
    validation_method: Optional[str] = None
    validation_option: Optional[Sequence[ValidationOption]] = None


