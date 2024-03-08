from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sqs_privilege_type = Union[Literal["DeleteQueue"], Literal["ListMessageMoveTasks"], Literal["DeleteMessage"], Literal["ListDeadLetterSourceQueues"], Literal["SendMessage"], Literal["GetQueueAttributes"], Literal["RemovePermission"], Literal["ReceiveMessage"], Literal["StartMessageMoveTask"], Literal["SetQueueAttributes"], Literal["TagQueue"], Literal["AddPermission"], Literal["ListQueues"], Literal["GetQueueUrl"], Literal["CancelMessageMoveTask"], Literal["CreateQueue"], Literal["ListQueueTags"], Literal["UntagQueue"], Literal["ChangeMessageVisibility"], Literal["PurgeQueue"]]
aws_sqs_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_sqsStatement(GenericResourceType[aws_sqs_privilege_type, aws_sqs_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    