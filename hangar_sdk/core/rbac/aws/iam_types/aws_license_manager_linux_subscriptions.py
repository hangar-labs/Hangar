from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_license_manager_linux_subscriptions_privilege_type = Union[Literal["ListLinuxSubscriptions"], Literal["ListLinuxSubscriptionInstances"], Literal["GetServiceSettings"], Literal["UpdateServiceSettings"]]
aws_license_manager_linux_subscriptions_condition_type = None

class aws_license_manager_linux_subscriptionsStatement(GenericResourceType[aws_license_manager_linux_subscriptions_privilege_type, aws_license_manager_linux_subscriptions_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    