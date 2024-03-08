from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codecatalyst_privilege_type = Union[Literal["CreateIdentityCenterApplication"], Literal["AssociateIamRoleToConnection"], Literal["UntagResource"], Literal["CreateSpace"], Literal["ListIdentityCenterApplications"], Literal["DeleteIdentityCenterApplication"], Literal["GetPendingConnection"], Literal["GetBillingAuthorization"], Literal["SynchronizeIdentityCenterApplication"], Literal["DeleteConnection"], Literal["GetConnection"], Literal["CreateSpaceAdminRoleAssignment"], Literal["BatchDisassociateIdentitiesFromIdentityCenterApplication"], Literal["ListTagsForResource"], Literal["RejectConnection"], Literal["AssociateIdentityToIdentityCenterApplication"], Literal["AssociateIdentityCenterApplicationToSpace"], Literal["ListSpacesForIdentityCenterApplication"], Literal["ListConnections"], Literal["AcceptConnection"], Literal["DisassociateIdentityCenterApplicationFromSpace"], Literal["ListIdentityCenterApplicationsForSpace"], Literal["DisassociateIdentityFromIdentityCenterApplication"], Literal["BatchAssociateIdentitiesToIdentityCenterApplication"], Literal["UpdateIdentityCenterApplication"], Literal["ListIamRolesForConnection"], Literal["TagResource"], Literal["PutBillingAuthorization"], Literal["DisassociateIamRoleFromConnection"], Literal["GetIdentityCenterApplication"]]
aws_codecatalyst_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codecatalystStatement(GenericResourceType[aws_codecatalyst_privilege_type, aws_codecatalyst_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    