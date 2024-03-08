from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ts_privilege_type = Union[Literal["StartExecution"], Literal["GetExecutionOutput"], Literal["GetTool"], Literal["UntagResource"], Literal["TagResource"], Literal["ListExecutions"], Literal["ListTagsForResource"], Literal["ListTools"], Literal["GetExecution"]]
aws_ts_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_tsStatement(GenericResourceType[aws_ts_privilege_type, aws_ts_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    