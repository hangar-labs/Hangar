from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_identity_sync_privilege_type = Union[Literal["CreateSyncFilter"], Literal["UpdateSyncTarget"], Literal["ListSyncFilters"], Literal["CreateSyncProfile"], Literal["DeleteSyncTarget"], Literal["StartSync"], Literal["GetSyncTarget"], Literal["GetSyncProfile"], Literal["DeleteSyncProfile"], Literal["CreateSyncTarget"], Literal["StopSync"], Literal["DeleteSyncFilter"]]
aws_identity_sync_condition_type = None

class aws_identity_syncStatement(GenericResourceType[aws_identity_sync_privilege_type, aws_identity_sync_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    