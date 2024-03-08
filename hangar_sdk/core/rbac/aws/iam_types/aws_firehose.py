from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_firehose_privilege_type = Union[Literal["CreateDeliveryStream"], Literal["DescribeDeliveryStream"], Literal["TagDeliveryStream"], Literal["ListDeliveryStreams"], Literal["ListTagsForDeliveryStream"], Literal["StopDeliveryStreamEncryption"], Literal["PutRecord"], Literal["PutRecordBatch"], Literal["StartDeliveryStreamEncryption"], Literal["UpdateDestination"], Literal["UntagDeliveryStream"], Literal["DeleteDeliveryStream"]]
aws_firehose_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_firehoseStatement(GenericResourceType[aws_firehose_privilege_type, aws_firehose_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    