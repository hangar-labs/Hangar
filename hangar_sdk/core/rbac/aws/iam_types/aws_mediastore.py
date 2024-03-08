from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediastore_privilege_type = Union[Literal["StopAccessLogging"], Literal["UntagResource"], Literal["DescribeObject"], Literal["GetLifecyclePolicy"], Literal["PutObject"], Literal["DeleteObject"], Literal["PutContainerPolicy"], Literal["ListTagsForResource"], Literal["DeleteContainerPolicy"], Literal["DeleteLifecyclePolicy"], Literal["DeleteCorsPolicy"], Literal["GetCorsPolicy"], Literal["PutCorsPolicy"], Literal["DeleteMetricPolicy"], Literal["ListItems"], Literal["PutMetricPolicy"], Literal["GetObject"], Literal["GetMetricPolicy"], Literal["StartAccessLogging"], Literal["DeleteContainer"], Literal["TagResource"], Literal["GetContainerPolicy"], Literal["DescribeContainer"], Literal["CreateContainer"], Literal["PutLifecyclePolicy"], Literal["ListContainers"]]
aws_mediastore_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediastoreStatement(GenericResourceType[aws_mediastore_privilege_type, aws_mediastore_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    