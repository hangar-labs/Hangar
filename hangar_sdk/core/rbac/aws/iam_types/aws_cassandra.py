from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cassandra_privilege_type = Union[Literal["Modify"], Literal["Alter"], Literal["UntagResource"], Literal["DropMultiRegionResource"], Literal["AlterMultiRegionResource"], Literal["ModifyMultiRegionResource"], Literal["TagResource"], Literal["Restore"], Literal["UpdatePartitioner"], Literal["TagMultiRegionResource"], Literal["RestoreMultiRegionTable"], Literal["CreateMultiRegionResource"], Literal["Create"], Literal["Drop"], Literal["UnTagMultiRegionResource"], Literal["Select"], Literal["SelectMultiRegionResource"]]
aws_cassandra_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cassandraStatement(GenericResourceType[aws_cassandra_privilege_type, aws_cassandra_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    