from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AuthenticationMode(AbstractTerraformBlock):
    passwords: Sequence[str]
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authentication_mode")


@define(kw_only=True, slots=False)
class AwsMemorydbUser(AbstractTerraformResource):
    _group: Any
    _top_name: str
    access_string: str
    user_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_memorydb_user")
    authentication_mode: Optional[Sequence[AuthenticationMode]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
