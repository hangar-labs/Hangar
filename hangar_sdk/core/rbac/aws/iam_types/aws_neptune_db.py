from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_neptune_db_privilege_type = Union[Literal["DeleteDataViaQuery"], Literal["ManageStatistics"], Literal["ListMLModelTransformJobs"], Literal["GetGraphSummary"], Literal["StartMLDataProcessingJob"], Literal["GetQueryStatus"], Literal["GetMLEndpointStatus"], Literal["GetLoaderJobStatus"], Literal["CreateMLEndpoint"], Literal["CancelLoaderJob"], Literal["DeleteStatistics"], Literal["GetStatisticsStatus"], Literal["ListMLDataProcessingJobs"], Literal["connect"], Literal["GetStreamRecords"], Literal["GetMLModelTrainingJobStatus"], Literal["ListLoaderJobs"], Literal["GetMLDataProcessingJobStatus"], Literal["DeleteMLEndpoint"], Literal["StartLoaderJob"], Literal["ListMLModelTrainingJobs"], Literal["GetMLModelTransformJobStatus"], Literal["CancelMLModelTrainingJob"], Literal["GetEngineStatus"], Literal["ReadDataViaQuery"], Literal["StartMLModelTrainingJob"], Literal["StartMLModelTransformJob"], Literal["CancelMLDataProcessingJob"], Literal["CancelQuery"], Literal["WriteDataViaQuery"], Literal["ListMLEndpoints"], Literal["ResetDatabase"], Literal["CancelMLModelTransformJob"]]
aws_neptune_db_condition_type = Union[Literal["neptune-db:QueryLanguage"]]

class aws_neptune_dbStatement(GenericResourceType[aws_neptune_db_privilege_type, aws_neptune_db_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    