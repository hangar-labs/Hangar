from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_kafka_cluster_privilege_type = Union[Literal["CreateTopic"], Literal["ReadData"], Literal["DescribeTransactionalId"], Literal["DescribeTopic"], Literal["AlterCluster"], Literal["DescribeClusterDynamicConfiguration"], Literal["AlterTopic"], Literal["Connect"], Literal["AlterTransactionalId"], Literal["DescribeCluster"], Literal["WriteData"], Literal["AlterGroup"], Literal["AlterTopicDynamicConfiguration"], Literal["DescribeTopicDynamicConfiguration"], Literal["WriteDataIdempotently"], Literal["DeleteTopic"], Literal["AlterClusterDynamicConfiguration"], Literal["DescribeGroup"], Literal["DeleteGroup"]]
aws_kafka_cluster_condition_type = None

class aws_kafka_clusterStatement(GenericResourceType[aws_kafka_cluster_privilege_type, aws_kafka_cluster_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    