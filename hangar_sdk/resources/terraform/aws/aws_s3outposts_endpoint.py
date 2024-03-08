from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3outpostsEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    outpost_id: str
    security_group_id: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3outposts_endpoint")
    access_type: Optional[str] = None
    customer_owned_ipv4_pool: Optional[str] = None
