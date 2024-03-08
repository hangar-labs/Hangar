from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_evidently_privilege_type = Union[Literal["CreateProject"], Literal["UpdateProjectDataDelivery"], Literal["GetExperiment"], Literal["UntagResource"], Literal["ListSegmentReferences"], Literal["UpdateFeature"], Literal["GetExperimentResults"], Literal["TestSegmentPattern"], Literal["BatchEvaluateFeature"], Literal["PutProjectEvents"], Literal["StopLaunch"], Literal["DeleteFeature"], Literal["CreateExperiment"], Literal["UpdateExperiment"], Literal["CreateFeature"], Literal["EvaluateFeature"], Literal["DeleteExperiment"], Literal["CreateLaunch"], Literal["GetFeature"], Literal["GetSegment"], Literal["ListExperiments"], Literal["ListTagsForResource"], Literal["StartExperiment"], Literal["ListProjects"], Literal["UpdateLaunch"], Literal["DeleteSegment"], Literal["DeleteLaunch"], Literal["UpdateProject"], Literal["DeleteProject"], Literal["StopExperiment"], Literal["ListLaunches"], Literal["GetProject"], Literal["CreateSegment"], Literal["TagResource"], Literal["StartLaunch"], Literal["GetLaunch"], Literal["ListSegments"], Literal["ListFeatures"]]
aws_evidently_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_evidentlyStatement(GenericResourceType[aws_evidently_privilege_type, aws_evidently_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    