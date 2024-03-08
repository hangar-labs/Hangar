from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_inspector_privilege_type = Union[Literal["StartAssessmentRun"], Literal["AddAttributesToFindings"], Literal["ListAssessmentTargets"], Literal["ListAssessmentRuns"], Literal["UpdateAssessmentTarget"], Literal["DescribeResourceGroups"], Literal["StopAssessmentRun"], Literal["ListExclusions"], Literal["RemoveAttributesFromFindings"], Literal["SetTagsForResource"], Literal["PreviewAgents"], Literal["ListRulesPackages"], Literal["ListEventSubscriptions"], Literal["DeleteAssessmentRun"], Literal["DeleteAssessmentTarget"], Literal["DescribeAssessmentRuns"], Literal["DescribeAssessmentTemplates"], Literal["ListTagsForResource"], Literal["GetExclusionsPreview"], Literal["CreateAssessmentTemplate"], Literal["ListAssessmentRunAgents"], Literal["DescribeExclusions"], Literal["ListAssessmentTemplates"], Literal["CreateResourceGroup"], Literal["CreateExclusionsPreview"], Literal["DescribeRulesPackages"], Literal["GetTelemetryMetadata"], Literal["ListFindings"], Literal["SubscribeToEvent"], Literal["UnsubscribeFromEvent"], Literal["DescribeAssessmentTargets"], Literal["DeleteAssessmentTemplate"], Literal["RegisterCrossAccountAccessRole"], Literal["GetAssessmentReport"], Literal["CreateAssessmentTarget"], Literal["DescribeFindings"], Literal["DescribeCrossAccountAccessRole"]]
aws_inspector_condition_type = None

class aws_inspectorStatement(GenericResourceType[aws_inspector_privilege_type, aws_inspector_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    