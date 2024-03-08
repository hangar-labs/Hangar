from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codestar_privilege_type = Union[Literal["DisassociateTeamMember"], Literal["CreateProject"], Literal["ListResources"], Literal["UpdateTeamMember"], Literal["UpdateUserProfile"], Literal["VerifyServiceRole"], Literal["DescribeUserProfile"], Literal["CreateUserProfile"], Literal["AssociateTeamMember"], Literal["ListTeamMembers"], Literal["ListProjects"], Literal["GetExtendedAccess"], Literal["ListUserProfiles"], Literal["DeleteExtendedAccess"], Literal["UpdateProject"], Literal["TagProject"], Literal["UntagProject"], Literal["DeleteUserProfile"], Literal["ListTagsForProject"], Literal["DeleteProject"], Literal["DescribeProject"], Literal["PutExtendedAccess"]]
aws_codestar_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codestarStatement(GenericResourceType[aws_codestar_privilege_type, aws_codestar_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    