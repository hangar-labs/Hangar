from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_machinelearning_privilege_type = Union[Literal["CreateDataSourceFromRedshift"], Literal["GetEvaluation"], Literal["UpdateEvaluation"], Literal["DescribeBatchPredictions"], Literal["DescribeTags"], Literal["DeleteMLModel"], Literal["CreateRealtimeEndpoint"], Literal["DeleteRealtimeEndpoint"], Literal["DeleteTags"], Literal["UpdateDataSource"], Literal["UpdateMLModel"], Literal["GetDataSource"], Literal["Predict"], Literal["GetMLModel"], Literal["CreateMLModel"], Literal["UpdateBatchPrediction"], Literal["DescribeDataSources"], Literal["DeleteEvaluation"], Literal["DeleteBatchPrediction"], Literal["AddTags"], Literal["GetBatchPrediction"], Literal["DescribeMLModels"], Literal["CreateEvaluation"], Literal["CreateBatchPrediction"], Literal["DescribeEvaluations"], Literal["CreateDataSourceFromRDS"], Literal["CreateDataSourceFromS3"], Literal["DeleteDataSource"]]
aws_machinelearning_condition_type = None

class aws_machinelearningStatement(GenericResourceType[aws_machinelearning_privilege_type, aws_machinelearning_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    