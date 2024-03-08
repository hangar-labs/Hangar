from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_lookoutvision_privilege_type = Union[Literal["CreateProject"], Literal["ListModelPackagingJobs"], Literal["DescribeModelPackagingJob"], Literal["UntagResource"], Literal["StartModelPackagingJob"], Literal["StopModel"], Literal["DescribeDataset"], Literal["DetectAnomalies"], Literal["CreateModel"], Literal["ListDatasetEntries"], Literal["DescribeModel"], Literal["DescribeTrialDetection"], Literal["ListTagsForResource"], Literal["CreateDataset"], Literal["ListProjects"], Literal["StartModel"], Literal["ListTrialDetections"], Literal["DeleteModel"], Literal["UpdateDatasetEntries"], Literal["DeleteProject"], Literal["ListModels"], Literal["DescribeProject"], Literal["TagResource"], Literal["StartTrialDetection"], Literal["DeleteDataset"]]
aws_lookoutvision_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_lookoutvisionStatement(GenericResourceType[aws_lookoutvision_privilege_type, aws_lookoutvision_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    