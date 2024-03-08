from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_workspaces_web_privilege_type = Union[Literal["ListTrustStores"], Literal["UpdateUserAccessLoggingSettings"], Literal["UntagResource"], Literal["ListPortals"], Literal["CreateUserAccessLoggingSettings"], Literal["GetIpAccessSettings"], Literal["AssociateNetworkSettings"], Literal["DeleteUserAccessLoggingSettings"], Literal["DisassociateNetworkSettings"], Literal["AssociateUserSettings"], Literal["GetBrowserSettings"], Literal["GetNetworkSettings"], Literal["GetPortal"], Literal["UpdateTrustStore"], Literal["UpdateNetworkSettings"], Literal["CreateBrowserSettings"], Literal["DeletePortal"], Literal["AssociateTrustStore"], Literal["AssociateBrowserSettings"], Literal["GetUserSettings"], Literal["UpdatePortal"], Literal["GetTrustStoreCertificate"], Literal["CreatePortal"], Literal["DisassociateUserAccessLoggingSettings"], Literal["ListBrowserSettings"], Literal["ListTagsForResource"], Literal["UpdateUserSettings"], Literal["GetTrustStore"], Literal["DeleteTrustStore"], Literal["ListTrustStoreCertificates"], Literal["ListUserAccessLoggingSettings"], Literal["GetPortalServiceProviderMetadata"], Literal["CreateIdentityProvider"], Literal["GetUserAccessLoggingSettings"], Literal["UpdateBrowserSettings"], Literal["DisassociateTrustStore"], Literal["ListIdentityProviders"], Literal["CreateIpAccessSettings"], Literal["AssociateUserAccessLoggingSettings"], Literal["DisassociateBrowserSettings"], Literal["GetIdentityProvider"], Literal["DisassociateUserSettings"], Literal["CreateNetworkSettings"], Literal["CreateUserSettings"], Literal["ListUserSettings"], Literal["DeleteBrowserSettings"], Literal["DeleteNetworkSettings"], Literal["DeleteIdentityProvider"], Literal["TagResource"], Literal["AssociateIpAccessSettings"], Literal["CreateTrustStore"], Literal["UpdateIpAccessSettings"], Literal["DeleteIpAccessSettings"], Literal["DisassociateIpAccessSettings"], Literal["ListNetworkSettings"], Literal["UpdateIdentityProvider"], Literal["ListIpAccessSettings"], Literal["DeleteUserSettings"]]
aws_workspaces_web_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_workspaces_webStatement(GenericResourceType[aws_workspaces_web_privilege_type, aws_workspaces_web_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    