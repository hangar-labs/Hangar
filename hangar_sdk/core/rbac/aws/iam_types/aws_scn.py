from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_scn_privilege_type = Union[Literal["AssignAdminPermissionsToUser"], Literal["ListInstances"], Literal["RemoveAdminPermissionsForUser"], Literal["UntagResource"], Literal["DeleteInstance"], Literal["TagResource"], Literal["DeleteSSOApplication"], Literal["DescribeInstance"], Literal["CreateSSOApplication"], Literal["ListTagsForResource"], Literal["ListAdminUsers"], Literal["UpdateInstance"], Literal["CreateInstance"]]
aws_scn_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_scnStatement(GenericResourceType[aws_scn_privilege_type, aws_scn_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    