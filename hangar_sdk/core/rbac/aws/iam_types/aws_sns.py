from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sns_privilege_type = Union[Literal["CreateTopic"], Literal["GetDataProtectionPolicy"], Literal["OptInPhoneNumber"], Literal["ListPlatformApplications"], Literal["UntagResource"], Literal["ListSMSSandboxPhoneNumbers"], Literal["ListTopics"], Literal["CreatePlatformEndpoint"], Literal["RemovePermission"], Literal["SetTopicAttributes"], Literal["CheckIfPhoneNumberIsOptedOut"], Literal["ListSubscriptionsByTopic"], Literal["GetEndpointAttributes"], Literal["ListTagsForResource"], Literal["GetSMSSandboxAccountStatus"], Literal["VerifySMSSandboxPhoneNumber"], Literal["SetEndpointAttributes"], Literal["Unsubscribe"], Literal["CreatePlatformApplication"], Literal["ConfirmSubscription"], Literal["SetSMSAttributes"], Literal["ListSubscriptions"], Literal["Publish"], Literal["ListOriginationNumbers"], Literal["AddPermission"], Literal["DeletePlatformApplication"], Literal["DeleteTopic"], Literal["CreateSMSSandboxPhoneNumber"], Literal["ListEndpointsByPlatformApplication"], Literal["GetTopicAttributes"], Literal["SetSubscriptionAttributes"], Literal["Subscribe"], Literal["DeleteEndpoint"], Literal["TagResource"], Literal["DeleteSMSSandboxPhoneNumber"], Literal["GetPlatformApplicationAttributes"], Literal["SetPlatformApplicationAttributes"], Literal["ListPhoneNumbersOptedOut"], Literal["GetSMSAttributes"], Literal["PutDataProtectionPolicy"], Literal["GetSubscriptionAttributes"]]
aws_sns_condition_type = Union[Literal["aws:TagKeys"], Literal["sns:Protocol"], Literal["sns:Endpoint"], Literal["aws:RequestTag/${TagKey}"]]

class aws_snsStatement(GenericResourceType[aws_sns_privilege_type, aws_sns_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    