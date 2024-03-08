from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailLbCertificate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    lb_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_lb_certificate")
    domain_name: Optional[str] = None
    subject_alternative_names: Optional[Sequence[str]] = None
