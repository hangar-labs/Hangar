from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_identitystore_auth_privilege_type = Union[Literal["BatchGetSession"], Literal["BatchDeleteSession"], Literal["ListSessions"]]
aws_identitystore_auth_condition_type = None

class aws_identitystore_authStatement(GenericResourceType[aws_identitystore_auth_privilege_type, aws_identitystore_auth_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    