from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_fms_privilege_type = Union[Literal["DeletePolicy"], Literal["DeleteResourceSet"], Literal["UntagResource"], Literal["GetComplianceDetail"], Literal["ListPolicies"], Literal["PutPolicy"], Literal["PutNotificationChannel"], Literal["BatchDisassociateResource"], Literal["AssociateAdminAccount"], Literal["PutAppsList"], Literal["BatchAssociateResource"], Literal["GetProtectionStatus"], Literal["ListMemberAccounts"], Literal["ListComplianceStatus"], Literal["GetResourceSet"], Literal["ListTagsForResource"], Literal["ListAdminAccountsForOrganization"], Literal["ListDiscoveredResources"], Literal["ListResourceSetResources"], Literal["DeleteAppsList"], Literal["ListProtocolsLists"], Literal["AssociateThirdPartyFirewall"], Literal["GetNotificationChannel"], Literal["ListThirdPartyFirewallFirewallPolicies"], Literal["DeleteProtocolsList"], Literal["GetAdminScope"], Literal["DisassociateThirdPartyFirewall"], Literal["GetPolicy"], Literal["ListAppsLists"], Literal["GetProtocolsList"], Literal["GetThirdPartyFirewallAssociationStatus"], Literal["PutResourceSet"], Literal["DisassociateAdminAccount"], Literal["GetAppsList"], Literal["PutProtocolsList"], Literal["TagResource"], Literal["ListAdminsManagingAccount"], Literal["ListResourceSets"], Literal["GetViolationDetails"], Literal["PutAdminAccount"], Literal["DeleteNotificationChannel"], Literal["GetAdminAccount"]]
aws_fms_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_fmsStatement(GenericResourceType[aws_fms_privilege_type, aws_fms_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    