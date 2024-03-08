from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codedeploy_commands_secure_privilege_type = Union[Literal["PollHostCommand"], Literal["PutHostCommandAcknowledgement"], Literal["PutHostCommandComplete"], Literal["GetDeploymentSpecification"]]
aws_codedeploy_commands_secure_condition_type = None

class aws_codedeploy_commands_secureStatement(GenericResourceType[aws_codedeploy_commands_secure_privilege_type, aws_codedeploy_commands_secure_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    