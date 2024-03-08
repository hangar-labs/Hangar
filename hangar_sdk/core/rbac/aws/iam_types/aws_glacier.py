from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_glacier_privilege_type = Union[Literal["DescribeVault"], Literal["RemoveTagsFromVault"], Literal["DeleteArchive"], Literal["DeleteVault"], Literal["GetVaultAccessPolicy"], Literal["InitiateMultipartUpload"], Literal["AddTagsToVault"], Literal["AbortMultipartUpload"], Literal["InitiateVaultLock"], Literal["UploadArchive"], Literal["SetDataRetrievalPolicy"], Literal["PurchaseProvisionedCapacity"], Literal["ListVaults"], Literal["AbortVaultLock"], Literal["GetDataRetrievalPolicy"], Literal["SetVaultAccessPolicy"], Literal["DeleteVaultNotifications"], Literal["GetJobOutput"], Literal["ListProvisionedCapacity"], Literal["SetVaultNotifications"], Literal["CompleteMultipartUpload"], Literal["UploadMultipartPart"], Literal["ListParts"], Literal["InitiateJob"], Literal["CreateVault"], Literal["GetVaultLock"], Literal["ListJobs"], Literal["ListMultipartUploads"], Literal["DeleteVaultAccessPolicy"], Literal["ListTagsForVault"], Literal["CompleteVaultLock"], Literal["DescribeJob"], Literal["GetVaultNotifications"]]
aws_glacier_condition_type = Union[Literal["aws:TagKeys"], Literal["glacier:ArchiveAgeInDays"], Literal["aws:RequestTag/${TagKey}"]]

class aws_glacierStatement(GenericResourceType[aws_glacier_privilege_type, aws_glacier_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    