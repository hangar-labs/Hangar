from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_securitylake_privilege_type = Union[Literal["DeleteDataLakeOrganizationConfiguration"], Literal["ListSubscribers"], Literal["GetDataLakeExceptionSubscription"], Literal["UntagResource"], Literal["GetSubscriber"], Literal["ListDataLakes"], Literal["CreateAwsLogSource"], Literal["DeleteSubscriber"], Literal["DeleteDataLake"], Literal["UpdateDataLake"], Literal["DeleteDataLakeExceptionSubscription"], Literal["CreateSubscriber"], Literal["ListTagsForResource"], Literal["GetDataLakeSources"], Literal["UpdateSubscriberNotification"], Literal["DeleteSubscriberNotification"], Literal["UpdateSubscriber"], Literal["ListLogSources"], Literal["CreateSubscriberNotification"], Literal["ListDataLakeExceptions"], Literal["CreateDataLake"], Literal["CreateDataLakeOrganizationConfiguration"], Literal["DeregisterDataLakeDelegatedAdministrator"], Literal["RegisterDataLakeDelegatedAdministrator"], Literal["TagResource"], Literal["CreateDataLakeExceptionSubscription"], Literal["GetDataLakeOrganizationConfiguration"], Literal["UpdateDataLakeExceptionSubscription"], Literal["DeleteAwsLogSource"], Literal["DeleteCustomLogSource"], Literal["CreateCustomLogSource"]]
aws_securitylake_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_securitylakeStatement(GenericResourceType[aws_securitylake_privilege_type, aws_securitylake_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    