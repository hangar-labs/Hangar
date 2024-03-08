from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_opsworks_cm_privilege_type = Union[Literal["UntagResource"], Literal["AssociateNode"], Literal["DescribeNodeAssociationStatus"], Literal["DisassociateNode"], Literal["DeleteBackup"], Literal["UpdateServerEngineAttributes"], Literal["CreateServer"], Literal["DescribeAccountAttributes"], Literal["DeleteServer"], Literal["CreateBackup"], Literal["ListTagsForResource"], Literal["ExportServerEngineAttribute"], Literal["RestoreServer"], Literal["DescribeEvents"], Literal["UpdateServer"], Literal["DescribeServers"], Literal["TagResource"], Literal["DescribeBackups"], Literal["StartMaintenance"]]
aws_opsworks_cm_condition_type = None

class aws_opsworks_cmStatement(GenericResourceType[aws_opsworks_cm_privilege_type, aws_opsworks_cm_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    