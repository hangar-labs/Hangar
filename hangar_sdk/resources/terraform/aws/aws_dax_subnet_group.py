from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDaxSubnetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dax_subnet_group")
    description: Optional[str] = None
