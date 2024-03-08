from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Optional,Sequence


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEfsMountTarget(AbstractTerraformResource):
    _group: Any
    _top_name: str
    file_system_id: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_mount_target")
    ip_address: Optional[str] = None
    security_groups: Optional[Sequence[str]] = None
    timeouts: Optional[Timeouts] = None


