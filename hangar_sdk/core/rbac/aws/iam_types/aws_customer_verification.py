from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_customer_verification_privilege_type = Union[Literal["CreateCustomerVerificationDetails"], Literal["GetCustomerVerificationDetails"], Literal["UpdateCustomerVerificationDetails"], Literal["GetCustomerVerificationEligibility"]]
aws_customer_verification_condition_type = None

class aws_customer_verificationStatement(GenericResourceType[aws_customer_verification_privilege_type, aws_customer_verification_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    