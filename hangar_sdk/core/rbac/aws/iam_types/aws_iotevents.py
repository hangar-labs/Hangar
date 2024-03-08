from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotevents_privilege_type = Union[Literal["UntagResource"], Literal["ListDetectors"], Literal["ListDetectorModels"], Literal["UpdateInput"], Literal["DescribeLoggingOptions"], Literal["DeleteAlarmModel"], Literal["GetDetectorModelAnalysisResults"], Literal["BatchAcknowledgeAlarm"], Literal["StartDetectorModelAnalysis"], Literal["CreateAlarmModel"], Literal["BatchSnoozeAlarm"], Literal["DescribeInput"], Literal["DeleteInput"], Literal["ListAlarmModelVersions"], Literal["UpdateAlarmModel"], Literal["DescribeDetectorModelAnalysis"], Literal["ListTagsForResource"], Literal["ListAlarmModels"], Literal["UpdateInputRouting"], Literal["CreateDetectorModel"], Literal["BatchEnableAlarm"], Literal["UpdateDetectorModel"], Literal["ListDetectorModelVersions"], Literal["BatchUpdateDetector"], Literal["BatchDeleteDetector"], Literal["DescribeDetector"], Literal["BatchPutMessage"], Literal["ListInputs"], Literal["ListAlarms"], Literal["DeleteDetectorModel"], Literal["TagResource"], Literal["DescribeAlarm"], Literal["BatchResetAlarm"], Literal["ListInputRoutings"], Literal["BatchDisableAlarm"], Literal["CreateInput"], Literal["PutLoggingOptions"], Literal["DescribeAlarmModel"], Literal["DescribeDetectorModel"]]
aws_iotevents_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ioteventsStatement(GenericResourceType[aws_iotevents_privilege_type, aws_iotevents_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    