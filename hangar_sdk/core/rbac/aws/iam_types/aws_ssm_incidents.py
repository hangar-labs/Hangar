from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ssm_incidents_privilege_type = Union[Literal["DeleteIncidentRecord"], Literal["UntagResource"], Literal["ListResponsePlans"], Literal["DeleteResponsePlan"], Literal["UpdateIncidentRecord"], Literal["GetResourcePolicies"], Literal["StartIncident"], Literal["UpdateResponsePlan"], Literal["UpdateRelatedItems"], Literal["ListReplicationSets"], Literal["GetIncidentRecord"], Literal["ListRelatedItems"], Literal["BatchGetIncidentFindings"], Literal["UpdateReplicationSet"], Literal["DeleteReplicationSet"], Literal["CreateReplicationSet"], Literal["ListTagsForResource"], Literal["ListIncidentRecords"], Literal["ListIncidentFindings"], Literal["PutResourcePolicy"], Literal["ListTimelineEvents"], Literal["UpdateTimelineEvent"], Literal["CreateTimelineEvent"], Literal["GetReplicationSet"], Literal["DeleteResourcePolicy"], Literal["TagResource"], Literal["DeleteTimelineEvent"], Literal["GetTimelineEvent"], Literal["CreateResponsePlan"], Literal["GetResponsePlan"], Literal["UpdateDeletionProtection"]]
aws_ssm_incidents_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ssm_incidentsStatement(GenericResourceType[aws_ssm_incidents_privilege_type, aws_ssm_incidents_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    