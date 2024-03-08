from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_notifications_privilege_type = Union[Literal["UpdateNotificationConfiguration"], Literal["UntagResource"], Literal["GetNotificationConfiguration"], Literal["ListNotificationHubs"], Literal["UpdateEventRule"], Literal["ListChannels"], Literal["DeleteEventRule"], Literal["GetEventRule"], Literal["ListNotificationEvents"], Literal["ListTagsForResource"], Literal["ListEventRules"], Literal["AssociateChannel"], Literal["DisassociateChannel"], Literal["CreateEventRule"], Literal["GetNotificationEvent"], Literal["RegisterNotificationHub"], Literal["CreateNotificationConfiguration"], Literal["DeregisterNotificationHub"], Literal["ListNotificationConfigurations"], Literal["TagResource"], Literal["DeleteNotificationConfiguration"]]
aws_notifications_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_notificationsStatement(GenericResourceType[aws_notifications_privilege_type, aws_notifications_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    