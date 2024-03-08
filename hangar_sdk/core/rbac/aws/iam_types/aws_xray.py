from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_xray_privilege_type = Union[Literal["GetDistinctTraceGraphs"], Literal["BatchGetTraces"], Literal["UpdateGroup"], Literal["UntagResource"], Literal["GetInsightImpactGraph"], Literal["GetTraceSummaries"], Literal["GetGroup"], Literal["Link"], Literal["GetSamplingStatisticSummaries"], Literal["GetSamplingTargets"], Literal["UpdateSamplingRule"], Literal["CreateGroup"], Literal["GetEncryptionConfig"], Literal["PutEncryptionConfig"], Literal["GetInsightEvents"], Literal["BatchGetTraceSummaryById"], Literal["ListTagsForResource"], Literal["GetServiceGraph"], Literal["GetInsightSummaries"], Literal["PutTraceSegments"], Literal["GetSamplingRules"], Literal["PutResourcePolicy"], Literal["CreateSamplingRule"], Literal["GetGroups"], Literal["DeleteSamplingRule"], Literal["ListResourcePolicies"], Literal["GetInsight"], Literal["PutTelemetryRecords"], Literal["DeleteGroup"], Literal["DeleteResourcePolicy"], Literal["TagResource"], Literal["GetTraceGraph"], Literal["GetTimeSeriesServiceStatistics"]]
aws_xray_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_xrayStatement(GenericResourceType[aws_xray_privilege_type, aws_xray_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    