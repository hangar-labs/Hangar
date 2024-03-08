from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_serviceextract_privilege_type = Union[Literal["GetConfig"]]
aws_serviceextract_condition_type = None

class aws_serviceextractStatement(GenericResourceType[aws_serviceextract_privilege_type, aws_serviceextract_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    