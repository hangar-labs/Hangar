from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_freertos_privilege_type = Union[Literal["CreateSubscription"], Literal["UpdateSoftwareConfiguration"], Literal["GetSoftwareURLForConfiguration"], Literal["VerifyEmail"], Literal["UpdateEmailRecipients"], Literal["ListSoftwarePatches"], Literal["ListSoftwareConfigurations"], Literal["ListHardwareVendors"], Literal["ListHardwarePlatforms"], Literal["DescribeHardwarePlatform"], Literal["ListFreeRTOSVersions"], Literal["GetEmpPatchUrl"], Literal["ListSubscriptions"], Literal["GetSoftwareURL"], Literal["DeleteSoftwareConfiguration"], Literal["DescribeSoftwareConfiguration"], Literal["ListSubscriptionEmails"], Literal["DescribeSubscription"], Literal["CreateSoftwareConfiguration"], Literal["GetSubscriptionBillingAmount"]]
aws_freertos_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_freertosStatement(GenericResourceType[aws_freertos_privilege_type, aws_freertos_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    