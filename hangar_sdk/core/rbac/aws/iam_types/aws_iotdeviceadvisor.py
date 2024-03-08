from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotdeviceadvisor_privilege_type = Union[Literal["UpdateSuiteDefinition"], Literal["GetSuiteRunReport"], Literal["CreateSuiteDefinition"], Literal["DeleteSuiteDefinition"], Literal["UntagResource"], Literal["GetEndpoint"], Literal["ListSuiteDefinitions"], Literal["TagResource"], Literal["GetSuiteRun"], Literal["ListSuiteRuns"], Literal["StopSuiteRun"], Literal["GetSuiteDefinition"], Literal["ListTagsForResource"], Literal["StartSuiteRun"]]
aws_iotdeviceadvisor_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iotdeviceadvisorStatement(GenericResourceType[aws_iotdeviceadvisor_privilege_type, aws_iotdeviceadvisor_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    