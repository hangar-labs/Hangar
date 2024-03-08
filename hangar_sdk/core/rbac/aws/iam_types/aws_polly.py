from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_polly_privilege_type = Union[Literal["DescribeVoices"], Literal["GetLexicon"], Literal["ListLexicons"], Literal["StartSpeechSynthesisTask"], Literal["GetSpeechSynthesisTask"], Literal["SynthesizeSpeech"], Literal["ListSpeechSynthesisTasks"], Literal["DeleteLexicon"], Literal["PutLexicon"]]
aws_polly_condition_type = None

class aws_pollyStatement(GenericResourceType[aws_polly_privilege_type, aws_polly_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    