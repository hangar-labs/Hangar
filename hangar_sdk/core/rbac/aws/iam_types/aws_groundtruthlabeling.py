from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_groundtruthlabeling_privilege_type = Union[Literal["RunFilterOrSampleDatasetJob"], Literal["AssociatePatchToManifestJob"], Literal["ListDatasetObjects"], Literal["RunGenerateManifestByCrawlingJob"], Literal["DescribeConsoleJob"]]
aws_groundtruthlabeling_condition_type = None

class aws_groundtruthlabelingStatement(GenericResourceType[aws_groundtruthlabeling_privilege_type, aws_groundtruthlabeling_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    