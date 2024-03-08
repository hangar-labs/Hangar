from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_inspector_scan_privilege_type = Union[Literal["ScanSbom"]]
aws_inspector_scan_condition_type = None

class aws_inspector_scanStatement(GenericResourceType[aws_inspector_scan_privilege_type, aws_inspector_scan_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    