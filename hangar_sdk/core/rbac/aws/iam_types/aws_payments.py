from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_payments_privilege_type = Union[Literal["MakePayment"], Literal["UpdatePaymentPreferences"], Literal["CreatePaymentInstrument"], Literal["GetPaymentInstrument"], Literal["DeletePaymentInstrument"], Literal["GetPaymentStatus"], Literal["ListPaymentPreferences"]]
aws_payments_condition_type = None

class aws_paymentsStatement(GenericResourceType[aws_payments_privilege_type, aws_payments_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    