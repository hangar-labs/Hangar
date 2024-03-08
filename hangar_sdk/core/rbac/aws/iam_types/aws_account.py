from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_account_privilege_type = Union[Literal["GetAccountInformation"], Literal["GetRegionOptStatus"], Literal["GetAlternateContact"], Literal["PutContactInformation"], Literal["PutAlternateContact"], Literal["DeleteAlternateContact"], Literal["PutChallengeQuestions"], Literal["CloseAccount"], Literal["GetContactInformation"], Literal["GetChallengeQuestions"], Literal["ListRegions"], Literal["EnableRegion"], Literal["DisableRegion"]]
aws_account_condition_type = Union[Literal["account:AlternateContactTypes"], Literal["account:TargetRegion"]]

class aws_accountStatement(GenericResourceType[aws_account_privilege_type, aws_account_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    