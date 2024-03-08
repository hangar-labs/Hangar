from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_supportapp_privilege_type = Union[Literal["DeleteAccountAlias"], Literal["DeleteSlackChannelConfiguration"], Literal["RedeemSlackOauthCode"], Literal["UpdateSlackChannelConfiguration"], Literal["DescribeSlackChannels"], Literal["RegisterSlackWorkspaceForOrganization"], Literal["CreateSlackChannelConfiguration"], Literal["ListSlackChannelConfigurations"], Literal["ListSlackWorkspaceConfigurations"], Literal["GetAccountAlias"], Literal["PutAccountAlias"], Literal["DeleteSlackWorkspaceConfiguration"], Literal["GetSlackOauthParameters"]]
aws_supportapp_condition_type = None

class aws_supportappStatement(GenericResourceType[aws_supportapp_privilege_type, aws_supportapp_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    