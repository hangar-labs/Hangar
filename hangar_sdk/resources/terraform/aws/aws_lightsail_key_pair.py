from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailKeyPair(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_key_pair")
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    pgp_key: Optional[str] = None
    public_key: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
