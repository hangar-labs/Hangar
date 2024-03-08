from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_networkmanager_chat_privilege_type = Union[Literal["SendConversationMessage"], Literal["NotifyConversationIsActive"], Literal["CreateConversation"], Literal["ListConversationMessages"], Literal["DeleteConversation"], Literal["ListConversations"], Literal["CancelMessageResponse"]]
aws_networkmanager_chat_condition_type = None

class aws_networkmanager_chatStatement(GenericResourceType[aws_networkmanager_chat_privilege_type, aws_networkmanager_chat_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    