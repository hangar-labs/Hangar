from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailLb(AbstractTerraformResource):
    _group: Any
    _top_name: str
    instance_port: int
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_lb")
    health_check_path: Optional[str] = None
    ip_address_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
