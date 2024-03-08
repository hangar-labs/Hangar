from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codeguru_profiler_privilege_type = Union[Literal["PostAgentProfile"], Literal["UntagResource"], Literal["BatchGetFrameMetricData"], Literal["GetNotificationConfiguration"], Literal["RemovePermission"], Literal["ListProfileTimes"], Literal["PutPermission"], Literal["ConfigureAgent"], Literal["RemoveNotificationChannel"], Literal["ListTagsForResource"], Literal["UpdateProfilingGroup"], Literal["GetRecommendations"], Literal["CreateProfilingGroup"], Literal["GetProfile"], Literal["SubmitFeedback"], Literal["DescribeProfilingGroup"], Literal["GetPolicy"], Literal["DeleteProfilingGroup"], Literal["ListProfilingGroups"], Literal["ListFindingsReports"], Literal["TagResource"], Literal["GetFindingsReportAccountSummary"], Literal["AddNotificationChannels"]]
aws_codeguru_profiler_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codeguru_profilerStatement(GenericResourceType[aws_codeguru_profiler_privilege_type, aws_codeguru_profiler_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    