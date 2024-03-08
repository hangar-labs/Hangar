from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sagemaker_groundtruth_synthetic_privilege_type = Union[Literal["GetAccountDetails"], Literal["CreateProject"], Literal["GetProject"], Literal["ListBatchDataTransfers"], Literal["StartBatchDataTransfer"], Literal["ListProjectDataTransfers"], Literal["ListProjectSummaries"], Literal["GetBatch"], Literal["StartProjectDataTransfer"], Literal["UpdateBatch"], Literal["DeleteProject"], Literal["ListBatchSummaries"]]
aws_sagemaker_groundtruth_synthetic_condition_type = None

class aws_sagemaker_groundtruth_syntheticStatement(GenericResourceType[aws_sagemaker_groundtruth_synthetic_privilege_type, aws_sagemaker_groundtruth_synthetic_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    