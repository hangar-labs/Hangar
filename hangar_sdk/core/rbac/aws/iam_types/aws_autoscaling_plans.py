from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_autoscaling_plans_privilege_type = Union[Literal["DescribeScalingPlans"], Literal["UpdateScalingPlan"], Literal["GetScalingPlanResourceForecastData"], Literal["CreateScalingPlan"], Literal["DescribeScalingPlanResources"], Literal["DeleteScalingPlan"]]
aws_autoscaling_plans_condition_type = None

class aws_autoscaling_plansStatement(GenericResourceType[aws_autoscaling_plans_privilege_type, aws_autoscaling_plans_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    