from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iot_device_tester_privilege_type = Union[Literal["SupportedVersion"], Literal["SendMetrics"], Literal["DownloadTestSuite"], Literal["LatestIdt"], Literal["CheckVersion"]]
aws_iot_device_tester_condition_type = None

class aws_iot_device_testerStatement(GenericResourceType[aws_iot_device_tester_privilege_type, aws_iot_device_tester_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    