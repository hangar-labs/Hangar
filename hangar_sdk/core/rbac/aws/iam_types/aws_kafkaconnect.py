from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_kafkaconnect_privilege_type = Union[Literal["DescribeConnector"], Literal["DescribeCustomPlugin"], Literal["ListConnectors"], Literal["CreateWorkerConfiguration"], Literal["ListCustomPlugins"], Literal["UpdateConnector"], Literal["CreateCustomPlugin"], Literal["CreateConnector"], Literal["DeleteConnector"], Literal["ListWorkerConfigurations"], Literal["DescribeWorkerConfiguration"], Literal["DeleteCustomPlugin"]]
aws_kafkaconnect_condition_type = None

class aws_kafkaconnectStatement(GenericResourceType[aws_kafkaconnect_privilege_type, aws_kafkaconnect_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    