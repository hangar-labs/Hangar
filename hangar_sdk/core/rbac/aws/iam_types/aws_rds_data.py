from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_rds_data_privilege_type = Union[Literal["BeginTransaction"], Literal["BatchExecuteStatement"], Literal["CommitTransaction"], Literal["RollbackTransaction"], Literal["ExecuteStatement"], Literal["ExecuteSql"]]
aws_rds_data_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"]]

class aws_rds_dataStatement(GenericResourceType[aws_rds_data_privilege_type, aws_rds_data_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    