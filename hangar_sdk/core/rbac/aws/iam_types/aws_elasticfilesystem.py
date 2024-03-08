from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elasticfilesystem_privilege_type = Union[Literal["DeleteFileSystemPolicy"], Literal["CreateFileSystem"], Literal["ClientRootAccess"], Literal["DescribeAccessPoints"], Literal["DescribeLifecycleConfiguration"], Literal["PutBackupPolicy"], Literal["DescribeReplicationConfigurations"], Literal["DescribeMountTargets"], Literal["UntagResource"], Literal["CreateTags"], Literal["DescribeBackupPolicy"], Literal["CreateReplicationConfiguration"], Literal["ModifyMountTargetSecurityGroups"], Literal["DescribeTags"], Literal["ClientWrite"], Literal["PutLifecycleConfiguration"], Literal["DeleteTags"], Literal["UpdateFileSystemProtection"], Literal["ClientMount"], Literal["Restore"], Literal["DescribeFileSystemPolicy"], Literal["ListTagsForResource"], Literal["UpdateFileSystem"], Literal["DescribeMountTargetSecurityGroups"], Literal["DescribeFileSystems"], Literal["PutAccountPreferences"], Literal["CreateMountTarget"], Literal["DeleteAccessPoint"], Literal["CreateAccessPoint"], Literal["PutFileSystemPolicy"], Literal["DeleteMountTarget"], Literal["DescribeAccountPreferences"], Literal["DeleteFileSystem"], Literal["DeleteReplicationConfiguration"], Literal["TagResource"], Literal["Backup"]]
aws_elasticfilesystem_condition_type = Union[Literal["aws:TagKeys"], Literal["elasticfilesystem:AccessPointArn"], Literal["elasticfilesystem:CreateAction"], Literal["elasticfilesystem:AccessedViaMountTarget"], Literal["elasticfilesystem:Encrypted"], Literal["aws:RequestTag/${TagKey}"]]

class aws_elasticfilesystemStatement(GenericResourceType[aws_elasticfilesystem_privilege_type, aws_elasticfilesystem_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    