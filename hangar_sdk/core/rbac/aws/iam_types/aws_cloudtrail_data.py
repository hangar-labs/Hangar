from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudtrail_data_privilege_type = Union[Literal["PutAuditEvents"]]
aws_cloudtrail_data_condition_type = None

class aws_cloudtrail_dataStatement(GenericResourceType[aws_cloudtrail_data_privilege_type, aws_cloudtrail_data_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    