from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_awsconnector_privilege_type = Union[Literal["RegisterConnector"], Literal["GetConnectorHealth"], Literal["ValidateConnectorId"]]
aws_awsconnector_condition_type = None

class aws_awsconnectorStatement(GenericResourceType[aws_awsconnector_privilege_type, aws_awsconnector_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    