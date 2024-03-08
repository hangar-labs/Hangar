from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sustainability_privilege_type = Union[Literal["GetCarbonFootprintSummary"]]
aws_sustainability_condition_type = None

class aws_sustainabilityStatement(GenericResourceType[aws_sustainability_privilege_type, aws_sustainability_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    