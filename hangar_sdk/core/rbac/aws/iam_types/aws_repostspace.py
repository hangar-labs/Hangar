from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_repostspace_privilege_type = Union[Literal["SendInvites"], Literal["UpdateSpace"], Literal["ListSpaces"], Literal["RegisterAdmin"], Literal["UntagResource"], Literal["CreateSpace"], Literal["GetSpace"], Literal["TagResource"], Literal["ListTagsForResource"], Literal["DeleteSpace"], Literal["DeregisterAdmin"]]
aws_repostspace_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_repostspaceStatement(GenericResourceType[aws_repostspace_privilege_type, aws_repostspace_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    