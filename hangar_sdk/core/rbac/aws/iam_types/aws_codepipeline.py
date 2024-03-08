from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codepipeline_privilege_type = Union[Literal["GetJobDetails"], Literal["PollForThirdPartyJobs"], Literal["UntagResource"], Literal["GetPipeline"], Literal["DisableStageTransition"], Literal["GetActionType"], Literal["PutWebhook"], Literal["EnableStageTransition"], Literal["CreatePipeline"], Literal["PutActionRevision"], Literal["GetPipelineState"], Literal["ListPipelineExecutions"], Literal["AcknowledgeThirdPartyJob"], Literal["ListActionExecutions"], Literal["RegisterWebhookWithThirdParty"], Literal["StartPipelineExecution"], Literal["ListTagsForResource"], Literal["PutApprovalResult"], Literal["DeletePipeline"], Literal["ListWebhooks"], Literal["StopPipelineExecution"], Literal["DeregisterWebhookWithThirdParty"], Literal["ListActionTypes"], Literal["PutThirdPartyJobSuccessResult"], Literal["AcknowledgeJob"], Literal["UpdatePipeline"], Literal["PutThirdPartyJobFailureResult"], Literal["DeleteCustomActionType"], Literal["RetryStageExecution"], Literal["PutJobSuccessResult"], Literal["GetThirdPartyJobDetails"], Literal["PollForJobs"], Literal["UpdateActionType"], Literal["TagResource"], Literal["CreateCustomActionType"], Literal["ListPipelines"], Literal["PutJobFailureResult"], Literal["GetPipelineExecution"], Literal["DeleteWebhook"]]
aws_codepipeline_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codepipelineStatement(GenericResourceType[aws_codepipeline_privilege_type, aws_codepipeline_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    