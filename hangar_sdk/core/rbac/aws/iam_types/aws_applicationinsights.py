from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_applicationinsights_privilege_type = Union[Literal["UntagResource"], Literal["DescribeApplication"], Literal["RemoveWorkload"], Literal["DescribeComponentConfiguration"], Literal["UpdateComponentConfiguration"], Literal["DescribeLogPattern"], Literal["Link"], Literal["ListProblems"], Literal["UpdateWorkload"], Literal["CreateApplication"], Literal["DescribeComponentConfigurationRecommendation"], Literal["CreateLogPattern"], Literal["UpdateApplication"], Literal["ListTagsForResource"], Literal["DeleteLogPattern"], Literal["DescribeWorkload"], Literal["DeleteComponent"], Literal["ListWorkloads"], Literal["UpdateLogPattern"], Literal["ListLogPatterns"], Literal["UpdateProblem"], Literal["AddWorkload"], Literal["DeleteApplication"], Literal["DescribeObservation"], Literal["ListApplications"], Literal["ListLogPatternSets"], Literal["ListComponents"], Literal["DescribeProblem"], Literal["CreateComponent"], Literal["UpdateComponent"], Literal["TagResource"], Literal["DescribeProblemObservations"], Literal["ListConfigurationHistory"], Literal["DescribeComponent"]]
aws_applicationinsights_condition_type = None

class aws_applicationinsightsStatement(GenericResourceType[aws_applicationinsights_privilege_type, aws_applicationinsights_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    