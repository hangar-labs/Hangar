from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_freetier_privilege_type = Union[Literal["GetFreeTierAlertPreference"], Literal["PutFreeTierAlertPreference"], Literal["GetFreeTierUsage"]]
aws_freetier_condition_type = None

class aws_freetierStatement(GenericResourceType[aws_freetier_privilege_type, aws_freetier_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    