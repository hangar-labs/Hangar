from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_detective_privilege_type = Union[Literal["BatchGetMembershipDatasources"], Literal["ListIndicators"], Literal["GetFreeTrialEligibility"], Literal["UntagResource"], Literal["DescribeOrganizationConfiguration"], Literal["ListMembers"], Literal["BatchGetGraphMemberDatasources"], Literal["GetInvestigation"], Literal["UpdateInvestigationState"], Literal["DeleteGraph"], Literal["InvokeAssistant"], Literal["DisableOrganizationAdminAccount"], Literal["ListGraphs"], Literal["GetGraphIngestState"], Literal["StartMonitoringMember"], Literal["CreateGraph"], Literal["UpdateDatasourcePackages"], Literal["ListTagsForResource"], Literal["GetMembers"], Literal["SearchGraph"], Literal["DisassociateMembership"], Literal["ListInvitations"], Literal["StartInvestigation"], Literal["AcceptInvitation"], Literal["DeleteMembers"], Literal["ListHighDegreeEntities"], Literal["ListDatasourcePackages"], Literal["ListOrganizationAdminAccount"], Literal["RejectInvitation"], Literal["TagResource"], Literal["CreateMembers"], Literal["UpdateOrganizationConfiguration"], Literal["ListInvestigations"], Literal["GetUsageInformation"], Literal["GetPricingInformation"], Literal["EnableOrganizationAdminAccount"]]
aws_detective_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_detectiveStatement(GenericResourceType[aws_detective_privilege_type, aws_detective_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    