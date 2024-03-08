from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53ZoneAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vpc_id: str
    zone_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_zone_association")
    vpc_region: Optional[str] = None
