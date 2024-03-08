from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_osis_privilege_type = Union[Literal["Ingest"], Literal["UntagResource"], Literal["StopPipeline"], Literal["TagResource"], Literal["GetPipeline"], Literal["GetPipelineBlueprint"], Literal["UpdatePipeline"], Literal["ListPipelineBlueprints"], Literal["StartPipeline"], Literal["ListTagsForResource"], Literal["GetPipelineChangeProgress"], Literal["ListPipelines"], Literal["CreatePipeline"], Literal["DeletePipeline"], Literal["ValidatePipeline"]]
aws_osis_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_osisStatement(GenericResourceType[aws_osis_privilege_type, aws_osis_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    