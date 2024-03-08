from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_dlm_privilege_type = Union[Literal["GetLifecyclePolicy"], Literal["DeleteLifecyclePolicy"], Literal["UntagResource"], Literal["TagResource"], Literal["CreateLifecyclePolicy"], Literal["ListTagsForResource"], Literal["GetLifecyclePolicies"], Literal["UpdateLifecyclePolicy"]]
aws_dlm_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_dlmStatement(GenericResourceType[aws_dlm_privilege_type, aws_dlm_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    