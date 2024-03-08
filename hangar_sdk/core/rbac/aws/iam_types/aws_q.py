from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_q_privilege_type = Union[Literal["StartTroubleshootingAnalysis"], Literal["StartConversation"], Literal["StartTroubleshootingResolutionExplanation"], Literal["GetConversation"], Literal["GetTroubleshootingResults"], Literal["SendMessage"]]
aws_q_condition_type = None

class aws_qStatement(GenericResourceType[aws_q_privilege_type, aws_q_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    