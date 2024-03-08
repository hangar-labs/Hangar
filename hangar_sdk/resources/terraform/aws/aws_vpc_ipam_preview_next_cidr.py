from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcIpamPreviewNextCidr(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ipam_pool_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipam_preview_next_cidr")
    disallowed_cidrs: Optional[Sequence[str]] = None
    netmask_length: Optional[int] = None
