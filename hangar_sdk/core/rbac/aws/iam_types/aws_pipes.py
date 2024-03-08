from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_pipes_privilege_type = Union[Literal["StartPipe"], Literal["DeletePipe"], Literal["UntagResource"], Literal["ListPipes"], Literal["TagResource"], Literal["DescribePipe"], Literal["CreatePipe"], Literal["ListTagsForResource"], Literal["UpdatePipe"], Literal["StopPipe"]]
aws_pipes_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_pipesStatement(GenericResourceType[aws_pipes_privilege_type, aws_pipes_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    