from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_emr_serverless_privilege_type = Union[Literal["ListTagsForResource"], Literal["GetApplication"], Literal["CreateApplication"], Literal["StartApplication"], Literal["UntagResource"], Literal["StopApplication"], Literal["TagResource"], Literal["DeleteApplication"], Literal["StartJobRun"], Literal["UpdateApplication"], Literal["CancelJobRun"], Literal["GetDashboardForJobRun"], Literal["AccessInteractiveEndpoints"], Literal["ListJobRuns"], Literal["ListApplications"], Literal["GetJobRun"]]
aws_emr_serverless_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_emr_serverlessStatement(GenericResourceType[aws_emr_serverless_privilege_type, aws_emr_serverless_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    