from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_marketplacecommerceanalytics_privilege_type = Union[Literal["StartSupportDataExport"], Literal["GenerateDataSet"]]
aws_marketplacecommerceanalytics_condition_type = None

class aws_marketplacecommerceanalyticsStatement(GenericResourceType[aws_marketplacecommerceanalytics_privilege_type, aws_marketplacecommerceanalytics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    