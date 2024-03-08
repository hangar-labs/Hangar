from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApprunnerCustomDomainAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_name: str
    service_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apprunner_custom_domain_association")
    enable_www_subdomain: Optional[bool] = None
