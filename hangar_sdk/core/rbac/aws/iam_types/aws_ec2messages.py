from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ec2messages_privilege_type = Union[Literal["SendReply"], Literal["GetEndpoint"], Literal["FailMessage"], Literal["AcknowledgeMessage"], Literal["DeleteMessage"], Literal["GetMessages"]]
aws_ec2messages_condition_type = Union[Literal["ssm:SourceInstanceARN"], Literal["ec2:SourceInstanceARN"]]

class aws_ec2messagesStatement(GenericResourceType[aws_ec2messages_privilege_type, aws_ec2messages_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    