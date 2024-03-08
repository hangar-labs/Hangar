from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_kinesis_privilege_type = Union[Literal["DescribeStreamConsumer"], Literal["ListTagsForStream"], Literal["DeleteStream"], Literal["GetRecords"], Literal["PutRecord"], Literal["CreateStream"], Literal["ListStreamConsumers"], Literal["DescribeLimits"], Literal["EnableEnhancedMonitoring"], Literal["MergeShards"], Literal["SplitShard"], Literal["ListShards"], Literal["DisableEnhancedMonitoring"], Literal["GetShardIterator"], Literal["UpdateStreamMode"], Literal["IncreaseStreamRetentionPeriod"], Literal["DescribeStreamSummary"], Literal["ListStreams"], Literal["PutRecords"], Literal["RegisterStreamConsumer"], Literal["DescribeStream"], Literal["UpdateShardCount"], Literal["PutResourcePolicy"], Literal["DeregisterStreamConsumer"], Literal["StopStreamEncryption"], Literal["RemoveTagsFromStream"], Literal["DeleteResourcePolicy"], Literal["StartStreamEncryption"], Literal["DecreaseStreamRetentionPeriod"], Literal["AddTagsToStream"], Literal["SubscribeToShard"], Literal["GetResourcePolicy"]]
aws_kinesis_condition_type = None

class aws_kinesisStatement(GenericResourceType[aws_kinesis_privilege_type, aws_kinesis_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    