from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudfront_keyvaluestore_privilege_type = Union[Literal["DescribeKeyValueStore"], Literal["UpdateKeys"], Literal["DeleteKey"], Literal["ListKeys"], Literal["GetKey"], Literal["PutKey"]]
aws_cloudfront_keyvaluestore_condition_type = None

class aws_cloudfront_keyvaluestoreStatement(GenericResourceType[aws_cloudfront_keyvaluestore_privilege_type, aws_cloudfront_keyvaluestore_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    