from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_supportplans_privilege_type = Union[Literal["CreateSupportPlanSchedule"], Literal["StartSupportPlanUpdate"], Literal["GetSupportPlanUpdateStatus"], Literal["GetSupportPlan"]]
aws_supportplans_condition_type = None

class aws_supportplansStatement(GenericResourceType[aws_supportplans_privilege_type, aws_supportplans_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    