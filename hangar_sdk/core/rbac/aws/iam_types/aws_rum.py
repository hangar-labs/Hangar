from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_rum_privilege_type = Union[Literal["PutRumEvents"], Literal["ListTagsForResource"], Literal["DeleteRumMetricsDestination"], Literal["GetAppMonitor"], Literal["UntagResource"], Literal["UpdateAppMonitor"], Literal["BatchCreateRumMetricDefinitions"], Literal["TagResource"], Literal["BatchDeleteRumMetricDefinitions"], Literal["CreateAppMonitor"], Literal["UpdateRumMetricDefinition"], Literal["PutRumMetricsDestination"], Literal["BatchGetRumMetricDefinitions"], Literal["DeleteAppMonitor"], Literal["ListRumMetricsDestinations"], Literal["ListAppMonitors"], Literal["GetAppMonitorData"]]
aws_rum_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_rumStatement(GenericResourceType[aws_rum_privilege_type, aws_rum_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    