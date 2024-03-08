from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elemental_support_cases_privilege_type = Union[Literal["CreateCase"], Literal["GetCases"], Literal["GetCase"], Literal["CheckCasePermission"], Literal["UpdateCase"]]
aws_elemental_support_cases_condition_type = None

class aws_elemental_support_casesStatement(GenericResourceType[aws_elemental_support_cases_privilege_type, aws_elemental_support_cases_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    