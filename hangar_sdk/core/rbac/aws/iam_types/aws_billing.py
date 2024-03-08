from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_billing_privilege_type = Union[Literal["GetIAMAccessPreference"], Literal["PutContractInformation"], Literal["GetBillingPreferences"], Literal["GetContractInformation"], Literal["GetBillingNotifications"], Literal["GetBillingData"], Literal["ListBillingViews"], Literal["UpdateIAMAccessPreference"], Literal["UpdateBillingPreferences"], Literal["GetCredits"], Literal["GetBillingDetails"], Literal["GetSellerOfRecord"], Literal["RedeemCredits"]]
aws_billing_condition_type = None

class aws_billingStatement(GenericResourceType[aws_billing_privilege_type, aws_billing_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    