from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_migrationhub_strategy_privilege_type = Union[Literal["ListAnalyzableServers"], Literal["GetApplicationComponentStrategies"], Literal["StartRecommendationReportGeneration"], Literal["GetPortfolioPreferences"], Literal["GetImportFileTask"], Literal["UpdateApplicationComponentConfig"], Literal["GetRecommendationReportDetails"], Literal["SendMessage"], Literal["GetPortfolioSummary"], Literal["ListJarArtifacts"], Literal["GetLatestAssessmentId"], Literal["GetServerDetails"], Literal["GetServerStrategies"], Literal["RegisterCollector"], Literal["GetAssessment"], Literal["GetApplicationComponentDetails"], Literal["StartImportFileTask"], Literal["PutPortfolioPreferences"], Literal["ListServers"], Literal["ListApplicationComponents"], Literal["ListAntiPatterns"], Literal["StartAssessment"], Literal["StopAssessment"], Literal["UpdateServerConfig"], Literal["UpdateCollectorConfiguration"], Literal["GetAntiPattern"], Literal["ListImportFileTask"], Literal["ListCollectors"], Literal["GetMessage"]]
aws_migrationhub_strategy_condition_type = None

class aws_migrationhub_strategyStatement(GenericResourceType[aws_migrationhub_strategy_privilege_type, aws_migrationhub_strategy_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    