from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_application_cost_profiler_privilege_type = Union[Literal["ImportApplicationUsage"], Literal["DeleteReportDefinition"], Literal["PutReportDefinition"], Literal["UpdateReportDefinition"], Literal["GetReportDefinition"], Literal["ListReportDefinitions"]]
aws_application_cost_profiler_condition_type = None

class aws_application_cost_profilerStatement(GenericResourceType[aws_application_cost_profiler_privilege_type, aws_application_cost_profiler_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    