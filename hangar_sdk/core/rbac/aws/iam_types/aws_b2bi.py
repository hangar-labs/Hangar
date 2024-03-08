from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_b2bi_privilege_type = Union[Literal["ListTransformers"], Literal["UntagResource"], Literal["UpdateTransformer"], Literal["CreateCapability"], Literal["DeletePartnership"], Literal["TestMapping"], Literal["UpdateCapability"], Literal["DeleteCapability"], Literal["DeleteProfile"], Literal["UpdateProfile"], Literal["ListTagsForResource"], Literal["ListCapabilities"], Literal["GetTransformerJob"], Literal["DeleteTransformer"], Literal["GetProfile"], Literal["CreatePartnership"], Literal["GetPartnership"], Literal["CreateTransformer"], Literal["CreateProfile"], Literal["UpdatePartnership"], Literal["StartTransformerJob"], Literal["GetTransformer"], Literal["GetCapability"], Literal["TagResource"], Literal["ListProfiles"], Literal["TestParsing"], Literal["ListPartnerships"]]
aws_b2bi_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_b2biStatement(GenericResourceType[aws_b2bi_privilege_type, aws_b2bi_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    