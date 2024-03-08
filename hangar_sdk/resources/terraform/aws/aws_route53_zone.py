from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Vpc(AbstractTerraformBlock):
    vpc_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vpc")
    vpc_region: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53Zone(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_zone")
    comment: Optional[str] = None
    delegation_set_id: Optional[str] = None
    force_destroy: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    vpc: Optional[Sequence[Vpc]] = None
