from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ssmmessages_privilege_type = Union[Literal["CreateControlChannel"], Literal["OpenDataChannel"], Literal["OpenControlChannel"], Literal["CreateDataChannel"]]
aws_ssmmessages_condition_type = Union[Literal["ssm:SourceInstanceARN"], Literal["ec2:SourceInstanceARN"]]

class aws_ssmmessagesStatement(GenericResourceType[aws_ssmmessages_privilege_type, aws_ssmmessages_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    