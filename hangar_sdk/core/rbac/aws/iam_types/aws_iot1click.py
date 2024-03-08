from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iot1click_privilege_type = Union[Literal["CreateProject"], Literal["UntagResource"], Literal["InvokeDeviceMethod"], Literal["ClaimDevicesByClaimCode"], Literal["ListPlacements"], Literal["UpdatePlacement"], Literal["CreatePlacement"], Literal["AssociateDeviceWithPlacement"], Literal["DisassociateDeviceFromPlacement"], Literal["ListDevices"], Literal["ListTagsForResource"], Literal["ListProjects"], Literal["DeletePlacement"], Literal["InitiateDeviceClaim"], Literal["UpdateDeviceState"], Literal["UpdateProject"], Literal["ListDeviceEvents"], Literal["UnclaimDevice"], Literal["DeleteProject"], Literal["GetDevicesInPlacement"], Literal["DescribeProject"], Literal["TagResource"], Literal["GetDeviceMethods"], Literal["FinalizeDeviceClaim"], Literal["DescribeDevice"], Literal["DescribePlacement"]]
aws_iot1click_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iot1clickStatement(GenericResourceType[aws_iot1click_privilege_type, aws_iot1click_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    