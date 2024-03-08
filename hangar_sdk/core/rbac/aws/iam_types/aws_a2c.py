from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_a2c_privilege_type = Union[Literal["StartContainerizationJob"], Literal["GetContainerizationJobDetails"], Literal["StartDeploymentJob"], Literal["GetDeploymentJobDetails"]]
aws_a2c_condition_type = None

class aws_a2cStatement(GenericResourceType[aws_a2c_privilege_type, aws_a2c_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    