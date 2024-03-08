from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_kendra_ranking_privilege_type = Union[Literal["DescribeRescoreExecutionPlan"], Literal["CreateRescoreExecutionPlan"], Literal["UntagResource"], Literal["DeleteRescoreExecutionPlan"], Literal["TagResource"], Literal["UpdateRescoreExecutionPlan"], Literal["Rescore"], Literal["ListTagsForResource"], Literal["ListRescoreExecutionPlans"]]
aws_kendra_ranking_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_kendra_rankingStatement(GenericResourceType[aws_kendra_ranking_privilege_type, aws_kendra_ranking_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    