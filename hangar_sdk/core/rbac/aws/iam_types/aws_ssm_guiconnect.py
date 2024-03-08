from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ssm_guiconnect_privilege_type = Union[Literal["GetConnection"], Literal["CancelConnection"], Literal["StartConnection"]]
aws_ssm_guiconnect_condition_type = None

class aws_ssm_guiconnectStatement(GenericResourceType[aws_ssm_guiconnect_privilege_type, aws_ssm_guiconnect_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    