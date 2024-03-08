from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_wickr_privilege_type = Union[Literal["ListNetworks"], Literal["UntagResource"], Literal["TagResource"], Literal["CreateAdminSession"], Literal["CreateNetwork"], Literal["ListTagsForResource"], Literal["UpdateNetworkDetails"]]
aws_wickr_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_wickrStatement(GenericResourceType[aws_wickr_privilege_type, aws_wickr_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    