from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_arc_zonal_shift_privilege_type = Union[Literal["GetManagedResource"], Literal["ListZonalShifts"], Literal["CancelZonalShift"], Literal["CreatePracticeRunConfiguration"], Literal["UpdatePracticeRunConfiguration"], Literal["UpdateZonalShift"], Literal["UpdateZonalAutoshiftConfiguration"], Literal["StartZonalShift"], Literal["ListAutoshifts"], Literal["DeletePracticeRunConfiguration"], Literal["ListManagedResources"]]
aws_arc_zonal_shift_condition_type = Union[Literal["aws:ResourceTag/${TagKey}"], Literal["elasticloadbalancing:ResourceTag/${TagKey}"]]

class aws_arc_zonal_shiftStatement(GenericResourceType[aws_arc_zonal_shift_privilege_type, aws_arc_zonal_shift_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    