from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iq_permission_privilege_type = Union[Literal["GetPermissionRequest"], Literal["AssumePermissionRole"], Literal["ListPermissionRequests"], Literal["RejectPermissionRequest"], Literal["RevokePermissionRequest"], Literal["ApprovePermissionRequest"], Literal["CreatePermissionRequest"], Literal["WithdrawPermissionRequest"], Literal["ApproveAccessGrant"]]
aws_iq_permission_condition_type = None

class aws_iq_permissionStatement(GenericResourceType[aws_iq_permission_privilege_type, aws_iq_permission_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    