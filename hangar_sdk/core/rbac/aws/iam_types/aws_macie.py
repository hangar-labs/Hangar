from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_macie_privilege_type = Union[Literal["AssociateS3Resources"], Literal["UpdateS3Resources"], Literal["DisassociateS3Resources"], Literal["ListMemberAccounts"], Literal["AssociateMemberAccount"], Literal["ListS3Resources"], Literal["DisassociateMemberAccount"]]
aws_macie_condition_type = Union[Literal["aws:SourceArn"]]

class aws_macieStatement(GenericResourceType[aws_macie_privilege_type, aws_macie_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    