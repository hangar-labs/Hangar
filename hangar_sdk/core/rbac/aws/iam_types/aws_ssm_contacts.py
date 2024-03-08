from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ssm_contacts_privilege_type = Union[Literal["DeleteRotation"], Literal["SendActivationCode"], Literal["UntagResource"], Literal["ListPageReceipts"], Literal["DeactivateContactChannel"], Literal["CreateRotation"], Literal["UpdateRotation"], Literal["GetContactPolicy"], Literal["AssociateContact"], Literal["CreateContactChannel"], Literal["DeleteContactChannel"], Literal["ListRotationOverrides"], Literal["GetContact"], Literal["ListPagesByEngagement"], Literal["GetContactChannel"], Literal["DeleteContact"], Literal["ListPageResolutions"], Literal["ListTagsForResource"], Literal["ActivateContactChannel"], Literal["ListEngagements"], Literal["CreateRotationOverride"], Literal["DeleteRotationOverride"], Literal["ListPagesByContact"], Literal["ListPreviewRotationShifts"], Literal["PutContactPolicy"], Literal["ListContactChannels"], Literal["ListRotationShifts"], Literal["AcceptPage"], Literal["StopEngagement"], Literal["UpdateContact"], Literal["TagResource"], Literal["DescribeEngagement"], Literal["GetRotationOverride"], Literal["CreateContact"], Literal["StartEngagement"], Literal["GetRotation"], Literal["UpdateContactChannel"], Literal["ListRotations"], Literal["DescribePage"], Literal["ListContacts"]]
aws_ssm_contacts_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ssm_contactsStatement(GenericResourceType[aws_ssm_contacts_privilege_type, aws_ssm_contacts_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    