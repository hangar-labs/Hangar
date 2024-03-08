from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codewhisperer_privilege_type = Union[Literal["DeleteCustomization"], Literal["AllowVendedLogDeliveryForResource"], Literal["ListCustomizations"], Literal["DeleteProfile"], Literal["ListCustomizationVersions"], Literal["UntagResource"], Literal["DisassociateCustomizationPermission"], Literal["TagResource"], Literal["CreateCustomization"], Literal["ListProfiles"], Literal["UpdateCustomization"], Literal["GenerateRecommendations"], Literal["GetCustomization"], Literal["UpdateProfile"], Literal["ListTagsForResource"], Literal["CreateProfile"], Literal["ListCustomizationPermissions"], Literal["AssociateCustomizationPermission"]]
aws_codewhisperer_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codewhispererStatement(GenericResourceType[aws_codewhisperer_privilege_type, aws_codewhisperer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    