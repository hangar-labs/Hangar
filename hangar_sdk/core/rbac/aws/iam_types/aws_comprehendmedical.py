from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_comprehendmedical_privilege_type = Union[Literal["DescribeRxNormInferenceJob"], Literal["StartPHIDetectionJob"], Literal["StartSNOMEDCTInferenceJob"], Literal["StopRxNormInferenceJob"], Literal["ListSNOMEDCTInferenceJobs"], Literal["StartEntitiesDetectionV2Job"], Literal["StartRxNormInferenceJob"], Literal["ListRxNormInferenceJobs"], Literal["InferSNOMEDCT"], Literal["ListPHIDetectionJobs"], Literal["ListICD10CMInferenceJobs"], Literal["DescribeICD10CMInferenceJob"], Literal["DescribeSNOMEDCTInferenceJob"], Literal["DetectEntitiesV2"], Literal["ListEntitiesDetectionV2Jobs"], Literal["DescribeEntitiesDetectionV2Job"], Literal["StopSNOMEDCTInferenceJob"], Literal["InferRxNorm"], Literal["StopEntitiesDetectionV2Job"], Literal["InferICD10CM"], Literal["StartICD10CMInferenceJob"], Literal["DescribePHIDetectionJob"], Literal["DetectPHI"], Literal["StopPHIDetectionJob"], Literal["StopICD10CMInferenceJob"]]
aws_comprehendmedical_condition_type = None

class aws_comprehendmedicalStatement(GenericResourceType[aws_comprehendmedical_privilege_type, aws_comprehendmedical_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    