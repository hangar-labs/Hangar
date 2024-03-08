from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cleanrooms_ml_privilege_type = Union[Literal["GetAudienceModel"], Literal["DeleteAudienceModel"], Literal["DeleteConfiguredAudienceModelPolicy"], Literal["GetAudienceGenerationJob"], Literal["DeleteAudienceGenerationJob"], Literal["ListConfiguredAudienceModels"], Literal["ListAudienceExportJobs"], Literal["StartAudienceExportJob"], Literal["StartAudienceGenerationJob"], Literal["DeleteTrainingDataset"], Literal["ListTagsForResource"], Literal["ListTrainingDatasets"], Literal["UnTagResource"], Literal["PutConfiguredAudienceModelPolicy"], Literal["DeleteConfiguredAudienceModel"], Literal["CreateAudienceModel"], Literal["ListAudienceModels"], Literal["ListAudienceGenerationJobs"], Literal["CreateTrainingDataset"], Literal["GetConfiguredAudienceModelPolicy"], Literal["TagResource"], Literal["CreateConfiguredAudienceModel"], Literal["GetConfiguredAudienceModel"], Literal["UpdateConfiguredAudienceModel"], Literal["GetTrainingDataset"]]
aws_cleanrooms_ml_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["cleanrooms-ml:CollaborationId"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cleanrooms_mlStatement(GenericResourceType[aws_cleanrooms_ml_privilege_type, aws_cleanrooms_ml_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    