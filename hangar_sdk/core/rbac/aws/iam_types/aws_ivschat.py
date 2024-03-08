from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ivschat_privilege_type = Union[Literal["UpdateRoom"], Literal["DisconnectUser"], Literal["UntagResource"], Literal["ListLoggingConfigurations"], Literal["ListRooms"], Literal["GetLoggingConfiguration"], Literal["CreateChatToken"], Literal["CreateLoggingConfiguration"], Literal["TagResource"], Literal["DeleteMessage"], Literal["DeleteRoom"], Literal["UpdateLoggingConfiguration"], Literal["CreateRoom"], Literal["ListTagsForResource"], Literal["DeleteLoggingConfiguration"], Literal["SendEvent"], Literal["GetRoom"]]
aws_ivschat_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ivschatStatement(GenericResourceType[aws_ivschat_privilege_type, aws_ivschat_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    