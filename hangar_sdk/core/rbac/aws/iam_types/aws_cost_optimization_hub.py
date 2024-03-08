from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cost_optimization_hub_privilege_type = Union[Literal["ListRecommendations"], Literal["GetPreferences"], Literal["GetRecommendation"], Literal["ListRecommendationSummaries"], Literal["ListEnrollmentStatuses"], Literal["UpdateEnrollmentStatus"], Literal["UpdatePreferences"]]
aws_cost_optimization_hub_condition_type = None

class aws_cost_optimization_hubStatement(GenericResourceType[aws_cost_optimization_hub_privilege_type, aws_cost_optimization_hub_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    