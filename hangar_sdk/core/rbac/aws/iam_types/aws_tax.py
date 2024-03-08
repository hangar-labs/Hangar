from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_tax_privilege_type = Union[Literal["GetTaxInheritance"], Literal["DeleteTaxRegistration"], Literal["GetTaxRegistrationDocument"], Literal["PutTaxInterview"], Literal["PutTaxRegistration"], Literal["UpdateExemptions"], Literal["GetTaxRegistration"], Literal["GetExemptions"], Literal["BatchPutTaxRegistration"], Literal["GetTaxInterview"], Literal["PutTaxInheritance"], Literal["ListTaxRegistrations"]]
aws_tax_condition_type = None

class aws_taxStatement(GenericResourceType[aws_tax_privilege_type, aws_tax_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    