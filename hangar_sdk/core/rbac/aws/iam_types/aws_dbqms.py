from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_dbqms_privilege_type = Union[Literal["DescribeQueryHistory"], Literal["CreateQueryHistory"], Literal["CreateTab"], Literal["UpdateFavoriteQuery"], Literal["UpdateTab"], Literal["UpdateQueryHistory"], Literal["CreateFavoriteQuery"], Literal["DeleteTab"], Literal["DescribeTabs"], Literal["DescribeFavoriteQueries"], Literal["GetQueryString"], Literal["DeleteFavoriteQueries"], Literal["DeleteQueryHistory"]]
aws_dbqms_condition_type = None

class aws_dbqmsStatement(GenericResourceType[aws_dbqms_privilege_type, aws_dbqms_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    