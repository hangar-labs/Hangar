from typing import Any, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53CidrLocation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cidr_blocks: Sequence[str]
    cidr_collection_id: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_cidr_location")
