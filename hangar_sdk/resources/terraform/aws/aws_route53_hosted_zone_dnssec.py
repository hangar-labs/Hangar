from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53HostedZoneDnssec(AbstractTerraformResource):
    _group: Any
    _top_name: str
    hosted_zone_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_hosted_zone_dnssec")
    signing_status: Optional[str] = None
