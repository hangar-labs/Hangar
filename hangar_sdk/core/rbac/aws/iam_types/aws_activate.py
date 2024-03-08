from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_activate_privilege_type = Union[Literal["GetContentInfo"], Literal["GetAccountContact"], Literal["GetMemberInfo"], Literal["CreateForm"], Literal["GetProgram"], Literal["GetCredits"], Literal["PutMemberInfo"], Literal["GetCosts"]]
aws_activate_condition_type = None

class aws_activateStatement(GenericResourceType[aws_activate_privilege_type, aws_activate_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    