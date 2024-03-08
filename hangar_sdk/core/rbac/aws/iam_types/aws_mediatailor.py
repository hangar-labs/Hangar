from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediatailor_privilege_type = Union[Literal["GetPrefetchSchedule"], Literal["UntagResource"], Literal["UpdateSourceLocation"], Literal["UpdateChannel"], Literal["ListSourceLocations"], Literal["CreatePrefetchSchedule"], Literal["DeleteChannelPolicy"], Literal["DeleteProgram"], Literal["CreateChannel"], Literal["PutPlaybackConfiguration"], Literal["ConfigureLogsForPlaybackConfiguration"], Literal["DeleteLiveSource"], Literal["DescribeSourceLocation"], Literal["CreateSourceLocation"], Literal["ListAlerts"], Literal["GetPlaybackConfiguration"], Literal["ListPlaybackConfigurations"], Literal["ListChannels"], Literal["UpdateLiveSource"], Literal["UpdateProgram"], Literal["DescribeProgram"], Literal["UpdateVodSource"], Literal["ConfigureLogsForChannel"], Literal["CreateProgram"], Literal["CreateVodSource"], Literal["StartChannel"], Literal["GetChannelPolicy"], Literal["ListPrefetchSchedules"], Literal["ListTagsForResource"], Literal["DeleteVodSource"], Literal["ListVodSources"], Literal["GetChannelSchedule"], Literal["DeleteSourceLocation"], Literal["DescribeVodSource"], Literal["CreateLiveSource"], Literal["StopChannel"], Literal["DescribeLiveSource"], Literal["DeletePrefetchSchedule"], Literal["PutChannelPolicy"], Literal["TagResource"], Literal["ListLiveSources"], Literal["DeleteChannel"], Literal["DescribeChannel"], Literal["DeletePlaybackConfiguration"]]
aws_mediatailor_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediatailorStatement(GenericResourceType[aws_mediatailor_privilege_type, aws_mediatailor_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    