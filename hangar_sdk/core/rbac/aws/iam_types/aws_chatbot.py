from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_chatbot_privilege_type = Union[Literal["GetMicrosoftTeamsChannelConfiguration"], Literal["ListMicrosoftTeamsChannelConfigurations"], Literal["DescribeSlackUserIdentities"], Literal["ListMicrosoftTeamsUserIdentities"], Literal["GetAccountPreferences"], Literal["DeleteChimeWebhookConfiguration"], Literal["RedeemSlackOauthCode"], Literal["DescribeSlackChannels"], Literal["GetMicrosoftTeamsOauthParameters"], Literal["ListMicrosoftTeamsConfiguredTeams"], Literal["DescribeChimeWebhookConfigurations"], Literal["GetSlackOauthParameters"], Literal["CreateChimeWebhookConfiguration"], Literal["CreateSlackChannelConfiguration"], Literal["UpdateMicrosoftTeamsChannelConfiguration"], Literal["DeleteMicrosoftTeamsUserIdentity"], Literal["CreateMicrosoftTeamsChannelConfiguration"], Literal["UpdateSlackChannelConfiguration"], Literal["DescribeSlackWorkspaces"], Literal["DeleteSlackUserIdentity"], Literal["UpdateAccountPreferences"], Literal["DeleteMicrosoftTeamsConfiguredTeam"], Literal["DeleteSlackChannelConfiguration"], Literal["DeleteMicrosoftTeamsChannelConfiguration"], Literal["DeleteSlackWorkspaceAuthorization"], Literal["UpdateChimeWebhookConfiguration"], Literal["RedeemMicrosoftTeamsOauthCode"], Literal["DescribeSlackChannelConfigurations"]]
aws_chatbot_condition_type = None

class aws_chatbotStatement(GenericResourceType[aws_chatbot_privilege_type, aws_chatbot_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    