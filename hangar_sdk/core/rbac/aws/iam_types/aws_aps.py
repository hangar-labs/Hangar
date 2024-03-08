from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_aps_privilege_type = Union[Literal["ListWorkspaces"], Literal["QueryMetrics"], Literal["PutRuleGroupsNamespace"], Literal["UntagResource"], Literal["ListScrapers"], Literal["UpdateLoggingConfiguration"], Literal["RemoteWrite"], Literal["GetAlertManagerSilence"], Literal["PutAlertManagerDefinition"], Literal["DeleteScraper"], Literal["ListAlertManagerSilences"], Literal["UpdateWorkspaceAlias"], Literal["ListAlertManagerAlertGroups"], Literal["CreateAlertManagerDefinition"], Literal["CreateWorkspace"], Literal["DescribeAlertManagerDefinition"], Literal["ListRuleGroupsNamespaces"], Literal["DeleteAlertManagerSilence"], Literal["PutAlertManagerSilences"], Literal["DescribeWorkspace"], Literal["CreateScraper"], Literal["DeleteRuleGroupsNamespace"], Literal["ListTagsForResource"], Literal["GetLabels"], Literal["CreateRuleGroupsNamespace"], Literal["DescribeRuleGroupsNamespace"], Literal["ListAlertManagerReceivers"], Literal["CreateLoggingConfiguration"], Literal["GetSeries"], Literal["GetAlertManagerStatus"], Literal["DeleteWorkspace"], Literal["GetDefaultScraperConfiguration"], Literal["DeleteAlertManagerDefinition"], Literal["TagResource"], Literal["DescribeLoggingConfiguration"], Literal["ListRules"], Literal["ListAlertManagerAlerts"], Literal["DeleteLoggingConfiguration"], Literal["DescribeScraper"], Literal["CreateAlertManagerAlerts"], Literal["GetMetricMetadata"], Literal["ListAlerts"]]
aws_aps_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_apsStatement(GenericResourceType[aws_aps_privilege_type, aws_aps_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    