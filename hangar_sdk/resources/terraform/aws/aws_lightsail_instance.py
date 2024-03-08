from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AddOn(AbstractTerraformBlock):
    snapshot_time: str
    status: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="add_on")


@define(kw_only=True, slots=False)
class AwsLightsailInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    blueprint_id: str
    bundle_id: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_instance")
    add_on: Optional[Sequence[AddOn]] = None
    ip_address_type: Optional[str] = None
    key_pair_name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    user_data: Optional[str] = None
