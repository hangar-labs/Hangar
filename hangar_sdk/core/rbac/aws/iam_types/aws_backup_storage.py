from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_backup_storage_privilege_type = Union[Literal["PutObject"], Literal["DescribeBackupJob"], Literal["StartObject"], Literal["UpdateObjectComplete"], Literal["GetChunk"], Literal["DeleteObjects"], Literal["GetObjectMetadata"], Literal["GetIncrementalBaseBackup"], Literal["ListObjects"], Literal["MountCapsule"], Literal["GetBaseBackup"], Literal["PutChunk"], Literal["ListChunks"], Literal["NotifyObjectComplete"], Literal["CommitBackupJob"]]
aws_backup_storage_condition_type = None

class aws_backup_storageStatement(GenericResourceType[aws_backup_storage_privilege_type, aws_backup_storage_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    