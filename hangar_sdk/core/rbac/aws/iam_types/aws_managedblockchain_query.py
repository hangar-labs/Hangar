from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_managedblockchain_query_privilege_type = Union[Literal["BatchGetTokenBalance"], Literal["GetTransaction"], Literal["ListTokenBalances"], Literal["ListTransactionEvents"], Literal["GetTokenBalance"], Literal["ListAssetContracts"], Literal["GetAssetContract"], Literal["ListTransactions"]]
aws_managedblockchain_query_condition_type = None

class aws_managedblockchain_queryStatement(GenericResourceType[aws_managedblockchain_query_privilege_type, aws_managedblockchain_query_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    