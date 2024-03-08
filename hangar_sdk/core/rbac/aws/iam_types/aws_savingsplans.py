from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_savingsplans_privilege_type = Union[Literal["DescribeSavingsPlansOfferingRates"], Literal["DescribeSavingsPlanRates"], Literal["UntagResource"], Literal["DeleteQueuedSavingsPlan"], Literal["TagResource"], Literal["DescribeSavingsPlans"], Literal["ListTagsForResource"], Literal["DescribeSavingsPlansOfferings"], Literal["CreateSavingsPlan"]]
aws_savingsplans_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_savingsplansStatement(GenericResourceType[aws_savingsplans_privilege_type, aws_savingsplans_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    