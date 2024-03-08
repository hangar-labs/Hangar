from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_bugbust_privilege_type = Union[Literal["CreateEvent"], Literal["ListProfilingGroups"], Literal["ListTagsForResource"], Literal["ListEventScores"], Literal["JoinEvent"], Literal["UntagResource"], Literal["ListBugs"], Literal["TagResource"], Literal["EvaluateProfilingGroups"], Literal["GetJoinEventStatus"], Literal["ListEvents"], Literal["ListEventParticipants"], Literal["UpdateWorkItem"], Literal["GetEvent"], Literal["ListPullRequests"], Literal["UpdateEvent"], Literal["UpdateWorkItemAdmin"]]
aws_bugbust_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_bugbustStatement(GenericResourceType[aws_bugbust_privilege_type, aws_bugbust_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    