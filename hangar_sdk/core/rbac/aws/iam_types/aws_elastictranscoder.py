from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elastictranscoder_privilege_type = Union[Literal["ReadJob"], Literal["ListJobsByPipeline"], Literal["ListJobsByStatus"], Literal["CreatePreset"], Literal["CancelJob"], Literal["CreateJob"], Literal["DeletePreset"], Literal["UpdatePipelineStatus"], Literal["ReadPipeline"], Literal["TestRole"], Literal["UpdatePipelineNotifications"], Literal["UpdatePipeline"], Literal["ListPresets"], Literal["ListPipelines"], Literal["CreatePipeline"], Literal["DeletePipeline"], Literal["ReadPreset"]]
aws_elastictranscoder_condition_type = None

class aws_elastictranscoderStatement(GenericResourceType[aws_elastictranscoder_privilege_type, aws_elastictranscoder_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    