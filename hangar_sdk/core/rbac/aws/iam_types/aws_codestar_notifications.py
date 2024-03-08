from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codestar_notifications_privilege_type = Union[Literal["ListEventTypes"], Literal["ListNotificationRules"], Literal["UntagResource"], Literal["DeleteNotificationRule"], Literal["Subscribe"], Literal["TagResource"], Literal["ListTargets"], Literal["ListTagsForResource"], Literal["Unsubscribe"], Literal["UpdateNotificationRule"], Literal["DeleteTarget"], Literal["CreateNotificationRule"], Literal["DescribeNotificationRule"]]
aws_codestar_notifications_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["codestar-notifications:NotificationsForResource"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codestar_notificationsStatement(GenericResourceType[aws_codestar_notifications_privilege_type, aws_codestar_notifications_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    