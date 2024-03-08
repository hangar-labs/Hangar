from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Dict,Optional,Sequence


@define(kw_only=True, slots=False)
class PosixUser(AbstractTerraformBlock):
    gid: int
    uid: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="posix_user")
    secondary_gids: Optional[Sequence[int]] = None


@define(kw_only=True, slots=False)
class CreationInfo(AbstractTerraformBlock):
    owner_gid: int
    owner_uid: int
    permissions: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="creation_info")


@define(kw_only=True, slots=False)
class RootDirectory(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="root_directory")
    creation_info: Optional[Sequence[CreationInfo]] = None
    path: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEfsAccessPoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    file_system_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_access_point")
    posix_user: Optional[Sequence[PosixUser]] = None
    root_directory: Optional[Sequence[RootDirectory]] = None
    tags: Optional[Dict[str,str]] = None
    tags_all: Optional[Dict[str,str]] = None


