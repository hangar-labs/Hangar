from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudhsm_privilege_type = Union[Literal["CreateLunaClient"], Literal["DeleteCluster"], Literal["ListHapgs"], Literal["UntagResource"], Literal["CopyBackupToRegion"], Literal["ListLunaClients"], Literal["DeleteHsm"], Literal["DescribeHsm"], Literal["CreateHapg"], Literal["DeleteLunaClient"], Literal["ListTags"], Literal["DeleteBackup"], Literal["ListHsms"], Literal["InitializeCluster"], Literal["RemoveTagsFromResource"], Literal["DescribeClusters"], Literal["ListAvailableZones"], Literal["ListTagsForResource"], Literal["GetConfig"], Literal["AddTagsToResource"], Literal["RestoreBackup"], Literal["DeleteHapg"], Literal["ModifyCluster"], Literal["ModifyHsm"], Literal["ModifyHapg"], Literal["DescribeLunaClient"], Literal["CreateCluster"], Literal["ModifyLunaClient"], Literal["TagResource"], Literal["ModifyBackupAttributes"], Literal["CreateHsm"], Literal["DescribeBackups"], Literal["DescribeHapg"]]
aws_cloudhsm_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cloudhsmStatement(GenericResourceType[aws_cloudhsm_privilege_type, aws_cloudhsm_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    