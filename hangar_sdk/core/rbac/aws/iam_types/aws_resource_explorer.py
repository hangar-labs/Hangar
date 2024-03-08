from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_resource_explorer_privilege_type = Union[Literal["ListTags"], Literal["ListResourceTypes"], Literal["ListResources"]]
aws_resource_explorer_condition_type = None

class aws_resource_explorerStatement(GenericResourceType[aws_resource_explorer_privilege_type, aws_resource_explorer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    