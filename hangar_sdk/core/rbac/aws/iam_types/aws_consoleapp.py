from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_consoleapp_privilege_type = Union[Literal["GetDeviceIdentity"], Literal["ListDeviceIdentities"]]
aws_consoleapp_condition_type = None

class aws_consoleappStatement(GenericResourceType[aws_consoleapp_privilege_type, aws_consoleapp_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    