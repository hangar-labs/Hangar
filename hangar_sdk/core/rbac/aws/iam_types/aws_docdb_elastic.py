from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_docdb_elastic_privilege_type = Union[Literal["CreateCluster"], Literal["CreateClusterSnapshot"], Literal["DeleteCluster"], Literal["UntagResource"], Literal["UpdateCluster"], Literal["TagResource"], Literal["GetCluster"], Literal["ListClusters"], Literal["DeleteClusterSnapshot"], Literal["ListTagsForResource"], Literal["GetClusterSnapshot"], Literal["RestoreClusterFromSnapshot"], Literal["ListClusterSnapshots"]]
aws_docdb_elastic_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_docdb_elasticStatement(GenericResourceType[aws_docdb_elastic_privilege_type, aws_docdb_elastic_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    