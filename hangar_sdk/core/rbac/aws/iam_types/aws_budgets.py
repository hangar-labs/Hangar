from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_budgets_privilege_type = Union[Literal["ModifyBudget"], Literal["CreateBudgetAction"], Literal["ViewBudget"], Literal["DescribeBudgetActionsForBudget"], Literal["ExecuteBudgetAction"], Literal["DescribeBudgetActionHistories"], Literal["DescribeBudgetAction"], Literal["DeleteBudgetAction"], Literal["UpdateBudgetAction"], Literal["DescribeBudgetActionsForAccount"]]
aws_budgets_condition_type = None

class aws_budgetsStatement(GenericResourceType[aws_budgets_privilege_type, aws_budgets_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    