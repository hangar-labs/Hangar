from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_rbin_privilege_type = Union[Literal["CreateRule"], Literal["UpdateRule"], Literal["UntagResource"], Literal["TagResource"], Literal["DeleteRule"], Literal["LockRule"], Literal["GetRule"], Literal["ListRules"], Literal["ListTagsForResource"], Literal["UnlockRule"]]
aws_rbin_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["rbin:Attribute/ResourceType"], Literal["aws:RequestTag/${TagKey}"]]

class aws_rbinStatement(GenericResourceType[aws_rbin_privilege_type, aws_rbin_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    