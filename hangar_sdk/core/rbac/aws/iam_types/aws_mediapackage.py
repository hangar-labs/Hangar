from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediapackage_privilege_type = Union[Literal["DescribeOriginEndpoint"], Literal["ListOriginEndpoints"], Literal["UntagResource"], Literal["UpdateChannel"], Literal["CreateHarvestJob"], Literal["CreateOriginEndpoint"], Literal["RotateChannelCredentials"], Literal["CreateChannel"], Literal["DescribeHarvestJob"], Literal["ListChannels"], Literal["UpdateOriginEndpoint"], Literal["ListTagsForResource"], Literal["ConfigureLogs"], Literal["RotateIngestEndpointCredentials"], Literal["DeleteOriginEndpoint"], Literal["ListHarvestJobs"], Literal["TagResource"], Literal["DeleteChannel"], Literal["DescribeChannel"]]
aws_mediapackage_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediapackageStatement(GenericResourceType[aws_mediapackage_privilege_type, aws_mediapackage_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    