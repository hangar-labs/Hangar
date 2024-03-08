from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_devops_guru_privilege_type = Union[Literal["DescribeServiceIntegration"], Literal["ListInsights"], Literal["ListEvents"], Literal["StartCostEstimation"], Literal["PutFeedback"], Literal["UpdateEventSourcesConfig"], Literal["UpdateServiceIntegration"], Literal["DescribeFeedback"], Literal["ListOrganizationInsights"], Literal["DescribeInsight"], Literal["GetCostEstimation"], Literal["DescribeAccountHealth"], Literal["DescribeEventSourcesConfig"], Literal["RemoveNotificationChannel"], Literal["SearchOrganizationInsights"], Literal["ListMonitoredResources"], Literal["ListNotificationChannels"], Literal["UpdateResourceCollection"], Literal["DescribeOrganizationResourceCollectionHealth"], Literal["SearchInsights"], Literal["ListAnomalousLogGroups"], Literal["DescribeOrganizationOverview"], Literal["DescribeResourceCollectionHealth"], Literal["ListRecommendations"], Literal["DescribeOrganizationHealth"], Literal["AddNotificationChannel"], Literal["DeleteInsight"], Literal["DescribeAnomaly"], Literal["GetResourceCollection"], Literal["ListAnomaliesForInsight"], Literal["DescribeAccountOverview"]]
aws_devops_guru_condition_type = Union[Literal["devops-guru:ServiceNames"]]

class aws_devops_guruStatement(GenericResourceType[aws_devops_guru_privilege_type, aws_devops_guru_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    