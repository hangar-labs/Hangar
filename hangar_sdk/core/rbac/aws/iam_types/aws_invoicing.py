from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_invoicing_privilege_type = Union[Literal["GetInvoicePDF"], Literal["ListInvoiceSummaries"], Literal["PutInvoiceEmailDeliveryPreferences"], Literal["GetInvoiceEmailDeliveryPreferences"]]
aws_invoicing_condition_type = None

class aws_invoicingStatement(GenericResourceType[aws_invoicing_privilege_type, aws_invoicing_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    