from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_scheduler_privilege_type = Union[Literal["GetSchedule"], Literal["ListTagsForResource"], Literal["GetScheduleGroup"], Literal["UntagResource"], Literal["ListScheduleGroups"], Literal["ListSchedules"], Literal["CreateScheduleGroup"], Literal["TagResource"], Literal["DeleteSchedule"], Literal["CreateSchedule"], Literal["DeleteScheduleGroup"], Literal["UpdateSchedule"]]
aws_scheduler_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_schedulerStatement(GenericResourceType[aws_scheduler_privilege_type, aws_scheduler_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    