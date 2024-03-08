from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_m2_privilege_type = Union[Literal["ListBatchJobExecutions"], Literal["UntagResource"], Literal["ListEnvironments"], Literal["GetApplicationVersion"], Literal["CreateEnvironment"], Literal["DeleteEnvironment"], Literal["StartBatchJob"], Literal["CreateDataSetImportTask"], Literal["ListDataSets"], Literal["CreateDeployment"], Literal["CreateApplication"], Literal["DeleteApplicationFromEnvironment"], Literal["GetSignedBluinsightsUrl"], Literal["ListApplicationVersions"], Literal["UpdateApplication"], Literal["GetEnvironment"], Literal["ListTagsForResource"], Literal["GetDataSetImportTask"], Literal["ListBatchJobDefinitions"], Literal["UpdateEnvironment"], Literal["ListEngineVersions"], Literal["DeleteApplication"], Literal["ListApplications"], Literal["GetBatchJobExecution"], Literal["CancelBatchJobExecution"], Literal["GetApplication"], Literal["GetDeployment"], Literal["ListDeployments"], Literal["StopApplication"], Literal["TagResource"], Literal["GetDataSetDetails"], Literal["StartApplication"], Literal["ListDataSetImportHistory"]]
aws_m2_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_m2Statement(GenericResourceType[aws_m2_privilege_type, aws_m2_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    