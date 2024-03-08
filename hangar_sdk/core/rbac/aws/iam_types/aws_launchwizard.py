from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_launchwizard_privilege_type = Union[Literal["PutSettingsSet"], Literal["ListAdditionalNodes"], Literal["ListDeploymentEvents"], Literal["ListProvisionedApps"], Literal["ListResourceCostEstimates"], Literal["CreateDeployment"], Literal["DeleteApp"], Literal["DeleteAdditionalNode"], Literal["GetInfrastructureSuggestion"], Literal["DescribeProvisionedApp"], Literal["DeleteSettingsSet"], Literal["DescribeAdditionalNode"], Literal["StartProvisioning"], Literal["ListWorkloadDeploymentPatterns"], Literal["ListWorkloads"], Literal["DescribeSettingsSet"], Literal["ListSettingsSets"], Literal["GetWorkloadAsset"], Literal["DescribeProvisioningEvents"], Literal["GetWorkloadAssets"], Literal["ListWorkloadDeploymentOptions"], Literal["GetWorkload"], Literal["GetResourceRecommendation"], Literal["GetIpAddress"], Literal["CreateSettingsSet"], Literal["UpdateSettingsSet"], Literal["GetDeployment"], Literal["ListAllowedResources"], Literal["ListDeployments"], Literal["GetResourceCostEstimate"], Literal["CreateAdditionalNode"], Literal["GetSettingsSet"], Literal["DeleteDeployment"]]
aws_launchwizard_condition_type = None

class aws_launchwizardStatement(GenericResourceType[aws_launchwizard_privilege_type, aws_launchwizard_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    