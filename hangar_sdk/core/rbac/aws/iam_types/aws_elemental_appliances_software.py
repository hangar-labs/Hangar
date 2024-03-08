from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elemental_appliances_software_privilege_type = Union[Literal["GetOrdersV2"], Literal["GetTaxes"], Literal["CompleteUpload"], Literal["ListTagsForResource"], Literal["UpdateQuote"], Literal["GetBillingAddresses"], Literal["UntagResource"], Literal["ListQuotes"], Literal["TagResource"], Literal["GetQuote"], Literal["SubmitOrderV1"], Literal["CreateQuote"], Literal["GetDeliveryAddressesV2"], Literal["CreateOrderV1"], Literal["GetAvsCorrectAddress"], Literal["GetOrder"], Literal["StartUpload"]]
aws_elemental_appliances_software_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_elemental_appliances_softwareStatement(GenericResourceType[aws_elemental_appliances_software_privilege_type, aws_elemental_appliances_software_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    