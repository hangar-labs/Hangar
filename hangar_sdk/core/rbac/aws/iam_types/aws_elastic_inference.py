from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elastic_inference_privilege_type = Union[Literal["DescribeAcceleratorOfferings"], Literal["UntagResource"], Literal["TagResource"], Literal["DescribeAcceleratorTypes"], Literal["ListTagsForResource"], Literal["DescribeAccelerators"], Literal["Connect"]]
aws_elastic_inference_condition_type = None

class aws_elastic_inferenceStatement(GenericResourceType[aws_elastic_inference_privilege_type, aws_elastic_inference_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    