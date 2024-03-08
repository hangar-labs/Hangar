from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_billingconductor_privilege_type = Union[Literal["UpdateCustomLineItem"], Literal["ListCustomLineItems"], Literal["UntagResource"], Literal["DeletePricingPlan"], Literal["UpdatePricingRule"], Literal["AssociateAccounts"], Literal["ListCustomLineItemVersions"], Literal["GetBillingGroupCostReport"], Literal["DeleteBillingGroup"], Literal["ListResourcesAssociatedToCustomLineItem"], Literal["DeleteCustomLineItem"], Literal["DisassociateAccounts"], Literal["UpdatePricingPlan"], Literal["CreateBillingGroup"], Literal["ListTagsForResource"], Literal["BatchDisassociateResourcesFromCustomLineItem"], Literal["AssociatePricingRules"], Literal["DeletePricingRule"], Literal["DisassociatePricingRules"], Literal["UpdateBillingGroup"], Literal["ListBillingGroups"], Literal["CreatePricingRule"], Literal["ListPricingPlans"], Literal["CreateCustomLineItem"], Literal["ListAccountAssociations"], Literal["ListPricingRules"], Literal["BatchAssociateResourcesToCustomLineItem"], Literal["ListPricingRulesAssociatedToPricingPlan"], Literal["TagResource"], Literal["ListPricingPlansAssociatedWithPricingRule"], Literal["ListBillingGroupCostReports"], Literal["CreatePricingPlan"]]
aws_billingconductor_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_billingconductorStatement(GenericResourceType[aws_billingconductor_privilege_type, aws_billingconductor_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    