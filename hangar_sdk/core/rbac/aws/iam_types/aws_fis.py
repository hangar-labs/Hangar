from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_fis_privilege_type = Union[Literal["InjectApiUnavailableError"], Literal["GetExperiment"], Literal["CreateTargetAccountConfiguration"], Literal["UntagResource"], Literal["DeleteExperimentTemplate"], Literal["ListTargetResourceTypes"], Literal["GetTargetAccountConfiguration"], Literal["GetTargetResourceType"], Literal["ListTargetAccountConfigurations"], Literal["ListExperiments"], Literal["StartExperiment"], Literal["CreateExperimentTemplate"], Literal["ListTagsForResource"], Literal["UpdateExperimentTemplate"], Literal["ListActions"], Literal["GetExperimentTemplate"], Literal["UpdateTargetAccountConfiguration"], Literal["GetAction"], Literal["GetExperimentTargetAccountConfiguration"], Literal["InjectApiInternalError"], Literal["DeleteTargetAccountConfiguration"], Literal["StopExperiment"], Literal["InjectApiThrottleError"], Literal["TagResource"], Literal["ListExperimentTemplates"], Literal["ListExperimentTargetAccountConfigurations"], Literal["ListExperimentResolvedTargets"]]
aws_fis_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["fis:Percentage"], Literal["fis:Service"], Literal["fis:Targets"], Literal["fis:Operations"], Literal["aws:RequestTag/${TagKey}"]]

class aws_fisStatement(GenericResourceType[aws_fis_privilege_type, aws_fis_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    