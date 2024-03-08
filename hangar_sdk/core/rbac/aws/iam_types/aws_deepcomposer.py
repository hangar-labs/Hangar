from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_deepcomposer_privilege_type = Union[Literal["ListSampleModels"], Literal["ListCompositions"], Literal["ListTagsForResource"], Literal["DeleteComposition"], Literal["AssociateCoupon"], Literal["CreateComposition"], Literal["UpdateComposition"], Literal["ListModels"], Literal["UntagResource"], Literal["UpdateModel"], Literal["GetComposition"], Literal["TagResource"], Literal["ListTrainingTopics"], Literal["GetModel"], Literal["CreateAudio"], Literal["DeleteModel"], Literal["GetSampleModel"], Literal["CreateModel"]]
aws_deepcomposer_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_deepcomposerStatement(GenericResourceType[aws_deepcomposer_privilege_type, aws_deepcomposer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    