from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailDisk(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    name: str
    size_in_gb: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_disk")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
