from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_finspace_api_privilege_type = Union[Literal["GetProgrammaticAccessCredentials"]]
aws_finspace_api_condition_type = None

class aws_finspace_apiStatement(GenericResourceType[aws_finspace_api_privilege_type, aws_finspace_api_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    