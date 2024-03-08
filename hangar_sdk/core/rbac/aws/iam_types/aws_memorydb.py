from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_memorydb_privilege_type = Union[Literal["CreateParameterGroup"], Literal["PurchaseReservedNodesOffering"], Literal["DeleteCluster"], Literal["UntagResource"], Literal["CreateSubnetGroup"], Literal["CreateUser"], Literal["UpdateSubnetGroup"], Literal["DescribeReservedNodes"], Literal["DescribeSubnetGroups"], Literal["ListTags"], Literal["CopySnapshot"], Literal["BatchUpdateCluster"], Literal["CreateAcl"], Literal["CreateSnapshot"], Literal["DescribeParameters"], Literal["DescribeClusters"], Literal["DeleteParameterGroup"], Literal["FailoverShard"], Literal["DescribeServiceUpdates"], Literal["Connect"], Literal["DeleteSubnetGroup"], Literal["DeleteUser"], Literal["UpdateAcl"], Literal["DescribeEvents"], Literal["DeleteAcl"], Literal["DescribeParameterGroups"], Literal["ResetParameterGroup"], Literal["CreateCluster"], Literal["DeleteSnapshot"], Literal["UpdateCluster"], Literal["DescribeUsers"], Literal["TagResource"], Literal["DescribeEngineVersions"], Literal["UpdateParameterGroup"], Literal["UpdateUser"], Literal["DescribeReservedNodesOfferings"], Literal["DescribeAcls"], Literal["DescribeSnapshots"], Literal["ListAllowedNodeTypeUpdates"]]
aws_memorydb_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_memorydbStatement(GenericResourceType[aws_memorydb_privilege_type, aws_memorydb_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    