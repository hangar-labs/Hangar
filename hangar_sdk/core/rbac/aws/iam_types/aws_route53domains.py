from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_route53domains_privilege_type = Union[Literal["RenewDomain"], Literal["ListTagsForDomain"], Literal["ListDomains"], Literal["DeleteTagsForDomain"], Literal["DisableDomainTransferLock"], Literal["ViewBilling"], Literal["EnableDomainAutoRenew"], Literal["UpdateDomainContactPrivacy"], Literal["UpdateDomainNameservers"], Literal["RejectDomainTransferFromAnotherAwsAccount"], Literal["CheckDomainTransferability"], Literal["TransferDomain"], Literal["CancelDomainTransferToAnotherAwsAccount"], Literal["ListPrices"], Literal["RegisterDomain"], Literal["EnableDomainTransferLock"], Literal["RetrieveDomainAuthCode"], Literal["AcceptDomainTransferFromAnotherAwsAccount"], Literal["TransferDomainToAnotherAwsAccount"], Literal["DisableDomainAutoRenew"], Literal["PushDomain"], Literal["CheckDomainAvailability"], Literal["AssociateDelegationSignerToDomain"], Literal["ListOperations"], Literal["DeleteDomain"], Literal["GetContactReachabilityStatus"], Literal["GetDomainSuggestions"], Literal["ResendContactReachabilityEmail"], Literal["UpdateDomainContact"], Literal["ResendOperationAuthorization"], Literal["GetDomainDetail"], Literal["UpdateTagsForDomain"], Literal["DisassociateDelegationSignerFromDomain"], Literal["GetOperationDetail"]]
aws_route53domains_condition_type = None

class aws_route53domainsStatement(GenericResourceType[aws_route53domains_privilege_type, aws_route53domains_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    