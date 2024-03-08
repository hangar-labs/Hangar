from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_migrationhub_orchestrator_privilege_type = Union[Literal["UntagResource"], Literal["CreateWorkflowStep"], Literal["GetTemplate"], Literal["SendMessage"], Literal["ListWorkflows"], Literal["GetTemplateStep"], Literal["GetWorkflowStepGroup"], Literal["CreateWorkflowStepGroup"], Literal["DeleteWorkflow"], Literal["UpdateWorkflowStepGroup"], Literal["ListTagsForResource"], Literal["StartWorkflow"], Literal["ListTemplateSteps"], Literal["RegisterPlugin"], Literal["ListWorkflowSteps"], Literal["GetWorkflow"], Literal["UpdateWorkflowStep"], Literal["RetryWorkflowStep"], Literal["GetTemplateStepGroup"], Literal["ListWorkflowStepGroups"], Literal["DeleteWorkflowStep"], Literal["DeleteWorkflowStepGroup"], Literal["TagResource"], Literal["CreateWorkflow"], Literal["GetWorkflowStep"], Literal["ListTemplates"], Literal["ListTemplateStepGroups"], Literal["StopWorkflow"], Literal["UpdateWorkflow"], Literal["GetMessage"], Literal["ListPlugins"]]
aws_migrationhub_orchestrator_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_migrationhub_orchestratorStatement(GenericResourceType[aws_migrationhub_orchestrator_privilege_type, aws_migrationhub_orchestrator_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    