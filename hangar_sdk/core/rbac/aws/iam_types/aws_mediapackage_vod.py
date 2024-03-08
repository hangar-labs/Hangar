from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediapackage_vod_privilege_type = Union[Literal["UpdatePackagingGroup"], Literal["ListTagsForResource"], Literal["DescribePackagingConfiguration"], Literal["UntagResource"], Literal["DescribeAsset"], Literal["DescribePackagingGroup"], Literal["CreateAsset"], Literal["ListPackagingConfigurations"], Literal["TagResource"], Literal["ListAssets"], Literal["DeleteAsset"], Literal["ListPackagingGroups"], Literal["ConfigureLogs"], Literal["CreatePackagingGroup"], Literal["DeletePackagingConfiguration"], Literal["CreatePackagingConfiguration"], Literal["DeletePackagingGroup"]]
aws_mediapackage_vod_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediapackage_vodStatement(GenericResourceType[aws_mediapackage_vod_privilege_type, aws_mediapackage_vod_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    