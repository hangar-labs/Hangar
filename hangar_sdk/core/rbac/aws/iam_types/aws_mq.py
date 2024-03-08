from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mq_privilege_type = Union[Literal["DescribeConfigurationRevision"], Literal["ListConfigurations"], Literal["CreateReplicaBroker"], Literal["CreateTags"], Literal["CreateUser"], Literal["Promote"], Literal["CreateBroker"], Literal["ListTags"], Literal["DeleteTags"], Literal["ListUsers"], Literal["ListBrokers"], Literal["CreateConfiguration"], Literal["DescribeBrokerEngineTypes"], Literal["ListConfigurationRevisions"], Literal["UpdateConfiguration"], Literal["DescribeUser"], Literal["DeleteBroker"], Literal["UpdateBroker"], Literal["DescribeBroker"], Literal["DescribeConfiguration"], Literal["DescribeBrokerInstanceOptions"], Literal["UpdateUser"], Literal["DeleteUser"], Literal["RebootBroker"]]
aws_mq_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mqStatement(GenericResourceType[aws_mq_privilege_type, aws_mq_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    