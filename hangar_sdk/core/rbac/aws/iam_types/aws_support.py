from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_support_privilege_type = Union[Literal["DescribeCommunication"], Literal["DescribeCreateCaseOptions"], Literal["RateCaseCommunication"], Literal["DescribeSupportedLanguages"], Literal["RefreshTrustedAdvisorCheck"], Literal["DescribeTrustedAdvisorCheckRefreshStatuses"], Literal["DescribeCases"], Literal["DescribeTrustedAdvisorChecks"], Literal["AddAttachmentsToSet"], Literal["DescribeSupportLevel"], Literal["DescribeIssueTypes"], Literal["InitiateCallForCase"], Literal["ResolveCase"], Literal["AddCommunicationToCase"], Literal["DescribeSeverityLevels"], Literal["DescribeCaseAttributes"], Literal["SearchForCases"], Literal["DescribeTrustedAdvisorCheckResult"], Literal["CreateCase"], Literal["DescribeTrustedAdvisorCheckSummaries"], Literal["DescribeAttachment"], Literal["DescribeServices"], Literal["PutCaseAttributes"], Literal["DescribeCommunications"], Literal["InitiateChatForCase"]]
aws_support_condition_type = None

class aws_supportStatement(GenericResourceType[aws_support_privilege_type, aws_support_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    