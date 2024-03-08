from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Optional,Sequence


@define(kw_only=True, slots=False)
class BackupPolicy(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="backup_policy")


@define(kw_only=True, slots=False)
class AwsEfsBackupPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    file_system_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_backup_policy")
    backup_policy: Optional[Sequence[BackupPolicy]] = None


