from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_application_transformation_privilege_type = Union[Literal["StartDeployment"], Literal["StartPortingRecommendationAssessment"], Literal["GetPortingRecommendationAssessment"], Literal["PutLogData"], Literal["StartGroupingAssessment"], Literal["GetDeployment"], Literal["GetPortingCompatibilityAssessment"], Literal["GetGroupingAssessment"], Literal["GetContainerization"], Literal["StartPortingCompatibilityAssessment"], Literal["GetRuntimeAssessment"], Literal["StartRuntimeAssessment"], Literal["StartContainerization"], Literal["PutMetricData"]]
aws_application_transformation_condition_type = None

class aws_application_transformationStatement(GenericResourceType[aws_application_transformation_privilege_type, aws_application_transformation_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    