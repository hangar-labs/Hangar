from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_airflow_privilege_type = Union[Literal["CreateCliToken"], Literal["UntagResource"], Literal["UpdateEnvironment"], Literal["ListEnvironments"], Literal["TagResource"], Literal["GetEnvironment"], Literal["DeleteEnvironment"], Literal["CreateEnvironment"], Literal["ListTagsForResource"], Literal["PublishMetrics"], Literal["CreateWebLoginToken"]]
aws_airflow_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_airflowStatement(GenericResourceType[aws_airflow_privilege_type, aws_airflow_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    