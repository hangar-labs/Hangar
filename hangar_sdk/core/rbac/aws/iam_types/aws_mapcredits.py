from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mapcredits_privilege_type = Union[Literal["ListAssociatedPrograms"], Literal["ListQuarterSpend"], Literal["ListQuarterCredits"]]
aws_mapcredits_condition_type = None

class aws_mapcreditsStatement(GenericResourceType[aws_mapcredits_privilege_type, aws_mapcredits_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    