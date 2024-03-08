from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_translate_privilege_type = Union[Literal["StartTextTranslationJob"], Literal["UntagResource"], Literal["GetParallelData"], Literal["ListTerminologies"], Literal["TranslateDocument"], Literal["ListTextTranslationJobs"], Literal["CreateParallelData"], Literal["UpdateParallelData"], Literal["ListTagsForResource"], Literal["StopTextTranslationJob"], Literal["ListLanguages"], Literal["DescribeTextTranslationJob"], Literal["DeleteTerminology"], Literal["DeleteParallelData"], Literal["ImportTerminology"], Literal["TagResource"], Literal["TranslateText"], Literal["GetTerminology"], Literal["ListParallelData"]]
aws_translate_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_translateStatement(GenericResourceType[aws_translate_privilege_type, aws_translate_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    