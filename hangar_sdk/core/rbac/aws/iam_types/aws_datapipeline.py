from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_datapipeline_privilege_type = Union[Literal["RemoveTags"], Literal["ReportTaskProgress"], Literal["DeactivatePipeline"], Literal["CreatePipeline"], Literal["GetPipelineDefinition"], Literal["ReportTaskRunnerHeartbeat"], Literal["EvaluateExpression"], Literal["QueryObjects"], Literal["DescribePipelines"], Literal["PutPipelineDefinition"], Literal["DeletePipeline"], Literal["ActivatePipeline"], Literal["DescribeObjects"], Literal["GetAccountLimits"], Literal["AddTags"], Literal["PollForTask"], Literal["ValidatePipelineDefinition"], Literal["SetStatus"], Literal["SetTaskStatus"], Literal["PutAccountLimits"], Literal["ListPipelines"]]
aws_datapipeline_condition_type = Union[Literal["datapipeline:PipelineCreator"], Literal["datapipeline:workerGroup"], Literal["datapipeline:Tag"]]

class aws_datapipelineStatement(GenericResourceType[aws_datapipeline_privilege_type, aws_datapipeline_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    