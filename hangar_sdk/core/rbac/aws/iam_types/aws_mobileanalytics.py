from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mobileanalytics_privilege_type = Union[Literal["GetReports"], Literal["GetFinancialReports"], Literal["PutEvents"]]
aws_mobileanalytics_condition_type = None

class aws_mobileanalyticsStatement(GenericResourceType[aws_mobileanalytics_privilege_type, aws_mobileanalytics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    