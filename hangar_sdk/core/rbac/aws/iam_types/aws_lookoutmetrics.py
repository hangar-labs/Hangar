from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_lookoutmetrics_privilege_type = Union[Literal["CreateMetricSet"], Literal["BackTestAnomalyDetector"], Literal["UntagResource"], Literal["PutFeedback"], Literal["DeleteAnomalyDetector"], Literal["UpdateAlert"], Literal["GetAnomalyGroup"], Literal["GetSampleData"], Literal["ListAnomalyGroupSummaries"], Literal["DescribeAnomalyDetectionExecutions"], Literal["DeactivateAnomalyDetector"], Literal["ListTagsForResource"], Literal["DeleteAlert"], Literal["UpdateAnomalyDetector"], Literal["CreateAnomalyDetector"], Literal["ActivateAnomalyDetector"], Literal["ListAnomalyDetectors"], Literal["CreateAlert"], Literal["DescribeAnomalyDetector"], Literal["ListMetricSets"], Literal["ListAnomalyGroupRelatedMetrics"], Literal["DescribeMetricSet"], Literal["DescribeAlert"], Literal["DetectMetricSetConfig"], Literal["ListAnomalyGroupTimeSeries"], Literal["UpdateMetricSet"], Literal["GetDataQualityMetrics"], Literal["TagResource"], Literal["GetFeedback"], Literal["ListAlerts"]]
aws_lookoutmetrics_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_lookoutmetricsStatement(GenericResourceType[aws_lookoutmetrics_privilege_type, aws_lookoutmetrics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    