from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Optional


@define(kw_only=True, slots=False)
class AwsEfsFileSystemPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    file_system_id: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_file_system_policy")
    bypass_policy_lockout_safety_check: Optional[bool] = None


