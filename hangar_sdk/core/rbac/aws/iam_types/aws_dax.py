from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_dax_privilege_type = Union[Literal["PutItem"], Literal["CreateParameterGroup"], Literal["DeleteCluster"], Literal["UntagResource"], Literal["CreateSubnetGroup"], Literal["RebootNode"], Literal["UpdateSubnetGroup"], Literal["BatchGetItem"], Literal["UpdateItem"], Literal["DescribeSubnetGroups"], Literal["ListTags"], Literal["DescribeParameters"], Literal["DescribeClusters"], Literal["DeleteParameterGroup"], Literal["ConditionCheckItem"], Literal["DeleteSubnetGroup"], Literal["DescribeEvents"], Literal["Query"], Literal["IncreaseReplicationFactor"], Literal["DescribeParameterGroups"], Literal["CreateCluster"], Literal["DecreaseReplicationFactor"], Literal["DeleteItem"], Literal["Scan"], Literal["TagResource"], Literal["DescribeDefaultParameters"], Literal["UpdateCluster"], Literal["GetItem"], Literal["BatchWriteItem"], Literal["UpdateParameterGroup"]]
aws_dax_condition_type = Union[Literal["dax:EnclosingOperation"]]

class aws_daxStatement(GenericResourceType[aws_dax_privilege_type, aws_dax_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    