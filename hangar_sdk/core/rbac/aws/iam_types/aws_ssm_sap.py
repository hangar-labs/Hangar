from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ssm_sap_privilege_type = Union[Literal["StartApplicationRefresh"], Literal["UntagResource"], Literal["GetComponent"], Literal["BackupDatabase"], Literal["RestoreDatabase"], Literal["DeregisterApplication"], Literal["ListTagsForResource"], Literal["ListDatabases"], Literal["UpdateHANABackupSettings"], Literal["GetOperation"], Literal["PutResourcePermission"], Literal["RegisterApplication"], Literal["ListApplications"], Literal["GetResourcePermission"], Literal["ListComponents"], Literal["DeleteResourcePermission"], Literal["GetApplication"], Literal["UpdateApplicationSettings"], Literal["ListOperations"], Literal["GetDatabase"], Literal["TagResource"]]
aws_ssm_sap_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ssm_sapStatement(GenericResourceType[aws_ssm_sap_privilege_type, aws_ssm_sap_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    