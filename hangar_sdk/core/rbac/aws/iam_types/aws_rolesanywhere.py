from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_rolesanywhere_privilege_type = Union[Literal["GetSubject"], Literal["UntagResource"], Literal["UpdateTrustAnchor"], Literal["EnableProfile"], Literal["DeleteProfile"], Literal["CreateTrustAnchor"], Literal["DeleteTrustAnchor"], Literal["ImportCrl"], Literal["UpdateProfile"], Literal["ListTagsForResource"], Literal["ResetNotificationSettings"], Literal["GetTrustAnchor"], Literal["EnableCrl"], Literal["GetProfile"], Literal["ListTrustAnchors"], Literal["DisableProfile"], Literal["ListCrls"], Literal["UpdateCrl"], Literal["DisableCrl"], Literal["DeleteCrl"], Literal["ListSubjects"], Literal["CreateProfile"], Literal["GetCrl"], Literal["PutNotificationSettings"], Literal["TagResource"], Literal["DisableTrustAnchor"], Literal["ListProfiles"], Literal["EnableTrustAnchor"]]
aws_rolesanywhere_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_rolesanywhereStatement(GenericResourceType[aws_rolesanywhere_privilege_type, aws_rolesanywhere_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    