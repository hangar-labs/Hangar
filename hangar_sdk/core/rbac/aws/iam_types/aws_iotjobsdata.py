from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotjobsdata_privilege_type = Union[Literal["StartNextPendingJobExecution"], Literal["UpdateJobExecution"], Literal["GetPendingJobExecutions"], Literal["DescribeJobExecution"]]
aws_iotjobsdata_condition_type = Union[Literal["iot:JobId"]]

class aws_iotjobsdataStatement(GenericResourceType[aws_iotjobsdata_privilege_type, aws_iotjobsdata_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    