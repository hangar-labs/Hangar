from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_pricing_privilege_type = Union[Literal["GetAttributeValues"], Literal["GetPriceListFileUrl"], Literal["DescribeServices"], Literal["ListPriceLists"], Literal["GetProducts"]]
aws_pricing_condition_type = None

class aws_pricingStatement(GenericResourceType[aws_pricing_privilege_type, aws_pricing_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    