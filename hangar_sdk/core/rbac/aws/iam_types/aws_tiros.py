from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_tiros_privilege_type = Union[Literal["CreateQuery"], Literal["ExtendQuery"], Literal["GetQueryAnswer"], Literal["GetQueryExplanation"], Literal["GetQueryExtensionAccounts"]]
aws_tiros_condition_type = None

class aws_tirosStatement(GenericResourceType[aws_tiros_privilege_type, aws_tiros_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    