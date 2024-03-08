from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_pi_privilege_type = Union[Literal["GetPerformanceAnalysisReport"], Literal["CreatePerformanceAnalysisReport"], Literal["DescribeDimensionKeys"], Literal["UntagResource"], Literal["TagResource"], Literal["DeletePerformanceAnalysisReport"], Literal["GetDimensionKeyDetails"], Literal["ListPerformanceAnalysisReports"], Literal["ListAvailableResourceMetrics"], Literal["ListTagsForResource"], Literal["GetResourceMetrics"], Literal["ListAvailableResourceDimensions"], Literal["GetResourceMetadata"]]
aws_pi_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_piStatement(GenericResourceType[aws_pi_privilege_type, aws_pi_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    