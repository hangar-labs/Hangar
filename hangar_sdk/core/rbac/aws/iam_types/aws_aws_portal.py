from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_aws_portal_privilege_type = Union[Literal["GetConsoleActionSetEnforced"], Literal["ViewUsage"], Literal["ModifyAccount"], Literal["ModifyPaymentMethods"], Literal["ViewBilling"], Literal["ViewAccount"], Literal["ViewPaymentMethods"], Literal["UpdateConsoleActionSetEnforced"], Literal["ModifyBilling"]]
aws_aws_portal_condition_type = None

class aws_aws_portalStatement(GenericResourceType[aws_aws_portal_privilege_type, aws_aws_portal_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    