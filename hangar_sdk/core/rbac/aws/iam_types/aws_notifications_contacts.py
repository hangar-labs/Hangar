from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_notifications_contacts_privilege_type = Union[Literal["ActivateEmailContact"], Literal["DeleteEmailContact"], Literal["SendActivationCode"], Literal["UntagResource"], Literal["TagResource"], Literal["GetEmailContact"], Literal["ListEmailContacts"], Literal["ListTagsForResource"], Literal["CreateEmailContact"]]
aws_notifications_contacts_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_notifications_contactsStatement(GenericResourceType[aws_notifications_contacts_privilege_type, aws_notifications_contacts_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    