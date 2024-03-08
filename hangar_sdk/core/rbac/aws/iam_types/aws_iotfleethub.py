from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotfleethub_privilege_type = Union[Literal["CreateApplication"], Literal["UntagResource"], Literal["DescribeApplication"], Literal["TagResource"], Literal["DeleteApplication"], Literal["UpdateApplication"], Literal["ListTagsForResource"], Literal["ListApplications"]]
aws_iotfleethub_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iotfleethubStatement(GenericResourceType[aws_iotfleethub_privilege_type, aws_iotfleethub_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    