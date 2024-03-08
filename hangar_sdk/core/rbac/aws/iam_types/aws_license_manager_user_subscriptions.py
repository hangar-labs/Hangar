from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_license_manager_user_subscriptions_privilege_type = Union[Literal["ListUserAssociations"], Literal["ListInstances"], Literal["StartProductSubscription"], Literal["ListProductSubscriptions"], Literal["UpdateIdentityProviderSettings"], Literal["StopProductSubscription"], Literal["ListIdentityProviders"], Literal["RegisterIdentityProvider"], Literal["DisassociateUser"], Literal["DeregisterIdentityProvider"], Literal["AssociateUser"]]
aws_license_manager_user_subscriptions_condition_type = None

class aws_license_manager_user_subscriptionsStatement(GenericResourceType[aws_license_manager_user_subscriptions_privilege_type, aws_license_manager_user_subscriptions_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    