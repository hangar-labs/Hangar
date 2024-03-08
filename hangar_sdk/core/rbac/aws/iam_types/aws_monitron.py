from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_monitron_privilege_type = Union[Literal["CreateProject"], Literal["ListProjectAdminUsers"], Literal["GetProject"], Literal["GetProjectAdminUser"], Literal["ListProjects"], Literal["UntagResource"], Literal["DeleteUserAccessRoleAssociation"], Literal["UpdateProject"], Literal["TagResource"], Literal["DeleteProjectUserAssociation"], Literal["AssociateProjectAdminUser"], Literal["ListProjectUserAssociations"], Literal["ListTagsForResource"], Literal["ListUserAccessRoleAssociations"], Literal["DisassociateProjectAdminUser"], Literal["DeleteProject"], Literal["CreateUserAccessRoleAssociation"], Literal["CreateProjectUserAssociation"]]
aws_monitron_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_monitronStatement(GenericResourceType[aws_monitron_privilege_type, aws_monitron_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    