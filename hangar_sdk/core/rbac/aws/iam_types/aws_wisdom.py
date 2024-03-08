from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_wisdom_privilege_type = Union[Literal["ListAssistants"], Literal["QueryAssistant"], Literal["UntagResource"], Literal["ListContents"], Literal["CreateAssistant"], Literal["ListKnowledgeBases"], Literal["StartImportJob"], Literal["NotifyRecommendationsReceived"], Literal["DeleteKnowledgeBase"], Literal["PutFeedback"], Literal["RemoveKnowledgeBaseTemplateUri"], Literal["DeleteContent"], Literal["GetSession"], Literal["GetAssistantAssociation"], Literal["GetContentSummary"], Literal["CreateSession"], Literal["CreateAssistantAssociation"], Literal["ListImportJobs"], Literal["DeleteAssistant"], Literal["GetImportJob"], Literal["ListTagsForResource"], Literal["SearchQuickResponses"], Literal["CreateKnowledgeBase"], Literal["ListAssistantAssociations"], Literal["GetRecommendations"], Literal["SearchContent"], Literal["DeleteQuickResponse"], Literal["GetQuickResponse"], Literal["DeleteImportJob"], Literal["UpdateQuickResponse"], Literal["CreateContent"], Literal["GetContent"], Literal["CreateQuickResponse"], Literal["SearchSessions"], Literal["StartContentUpload"], Literal["TagResource"], Literal["UpdateContent"], Literal["UpdateKnowledgeBaseTemplateUri"], Literal["GetKnowledgeBase"], Literal["DeleteAssistantAssociation"], Literal["ListQuickResponses"], Literal["GetAssistant"]]
aws_wisdom_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["wisdom:SearchFilter/RoutingProfileArn"], Literal["aws:RequestTag/${TagKey}"]]

class aws_wisdomStatement(GenericResourceType[aws_wisdom_privilege_type, aws_wisdom_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    