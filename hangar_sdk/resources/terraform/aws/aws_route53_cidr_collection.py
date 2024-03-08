from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53CidrCollection(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_cidr_collection")
