from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_partnercentral_account_management_privilege_type = Union[Literal["AssociatePartnerAccount"], Literal["AssociatePartnerUser"], Literal["DisassociatePartnerUser"]]
aws_partnercentral_account_management_condition_type = None

class aws_partnercentral_account_managementStatement(GenericResourceType[aws_partnercentral_account_management_privilege_type, aws_partnercentral_account_management_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    