from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_snow_device_management_privilege_type = Union[Literal["DescribeTask"], Literal["DescribeDeviceEc2Instances"], Literal["UntagResource"], Literal["DescribeExecution"], Literal["ListTasks"], Literal["ListDevices"], Literal["TagResource"], Literal["ListDeviceResources"], Literal["ListExecutions"], Literal["ListTagsForResource"], Literal["CancelTask"], Literal["DescribeDevice"], Literal["CreateTask"]]
aws_snow_device_management_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_snow_device_managementStatement(GenericResourceType[aws_snow_device_management_privilege_type, aws_snow_device_management_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    