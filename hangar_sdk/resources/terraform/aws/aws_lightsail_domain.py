from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailDomain(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_domain")
