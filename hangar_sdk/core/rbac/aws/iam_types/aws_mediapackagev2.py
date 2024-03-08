from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediapackagev2_privilege_type = Union[Literal["DeleteChannelGroup"], Literal["ListOriginEndpoints"], Literal["UntagResource"], Literal["UpdateChannel"], Literal["DeleteChannelPolicy"], Literal["CreateOriginEndpoint"], Literal["CreateChannel"], Literal["PutObject"], Literal["ListChannels"], Literal["GetChannelGroup"], Literal["UpdateOriginEndpoint"], Literal["GetChannelPolicy"], Literal["ListTagsForResource"], Literal["UpdateChannelGroup"], Literal["GetOriginEndpoint"], Literal["GetChannel"], Literal["DeleteOriginEndpoint"], Literal["CreateChannelGroup"], Literal["GetObject"], Literal["ListChannelGroups"], Literal["PutChannelPolicy"], Literal["TagResource"], Literal["GetHeadObject"], Literal["GetOriginEndpointPolicy"], Literal["PutOriginEndpointPolicy"], Literal["DeleteChannel"], Literal["DeleteOriginEndpointPolicy"]]
aws_mediapackagev2_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediapackagev2Statement(GenericResourceType[aws_mediapackagev2_privilege_type, aws_mediapackagev2_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    