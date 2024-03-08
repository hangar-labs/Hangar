from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_compute_optimizer_privilege_type = Union[Literal["GetRecommendationSummaries"], Literal["GetEnrollmentStatus"], Literal["GetLicenseRecommendations"], Literal["PutRecommendationPreferences"], Literal["DescribeRecommendationExportJobs"], Literal["GetECSServiceRecommendationProjectedMetrics"], Literal["ExportEBSVolumeRecommendations"], Literal["ExportEC2InstanceRecommendations"], Literal["ExportECSServiceRecommendations"], Literal["GetEffectiveRecommendationPreferences"], Literal["GetLambdaFunctionRecommendations"], Literal["GetEC2InstanceRecommendations"], Literal["GetAutoScalingGroupRecommendations"], Literal["ExportLicenseRecommendations"], Literal["GetRecommendationPreferences"], Literal["DeleteRecommendationPreferences"], Literal["ExportLambdaFunctionRecommendations"], Literal["GetECSServiceRecommendations"], Literal["GetEC2RecommendationProjectedMetrics"], Literal["GetEBSVolumeRecommendations"], Literal["ExportAutoScalingGroupRecommendations"], Literal["UpdateEnrollmentStatus"], Literal["GetEnrollmentStatusesForOrganization"]]
aws_compute_optimizer_condition_type = Union[Literal["compute-optimizer:ResourceType"]]

class aws_compute_optimizerStatement(GenericResourceType[aws_compute_optimizer_privilege_type, aws_compute_optimizer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    