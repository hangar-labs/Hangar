from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_access_analyzer_privilege_type = Union[Literal["ListAccessPreviews"], Literal["GetFindingsStatistics"], Literal["UpdateFindings"], Literal["CheckNoNewAccess"], Literal["GetGeneratedPolicy"], Literal["ListAnalyzers"], Literal["CreateArchiveRule"], Literal["UntagResource"], Literal["ApplyArchiveRule"], Literal["DeleteAnalyzer"], Literal["CreateAnalyzer"], Literal["StartResourceScan"], Literal["ListTagsForResource"], Literal["GetAnalyzedResource"], Literal["CreateAccessPreview"], Literal["CancelPolicyGeneration"], Literal["GetFinding"], Literal["StartPolicyGeneration"], Literal["ListFindings"], Literal["GetAccessPreview"], Literal["UpdateArchiveRule"], Literal["GetAnalyzer"], Literal["DeleteArchiveRule"], Literal["ListArchiveRules"], Literal["TagResource"], Literal["ListPolicyGenerations"], Literal["ValidatePolicy"], Literal["GetArchiveRule"], Literal["CheckAccessNotGranted"], Literal["ListAccessPreviewFindings"], Literal["ListAnalyzedResources"]]
aws_access_analyzer_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_access_analyzerStatement(GenericResourceType[aws_access_analyzer_privilege_type, aws_access_analyzer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    