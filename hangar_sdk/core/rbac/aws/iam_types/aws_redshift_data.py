from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_redshift_data_privilege_type = Union[Literal["ListSchemas"], Literal["BatchExecuteStatement"], Literal["DescribeTable"], Literal["ListStatements"], Literal["ExecuteStatement"], Literal["GetStatementResult"], Literal["ListTables"], Literal["ListDatabases"], Literal["CancelStatement"], Literal["DescribeStatement"]]
aws_redshift_data_condition_type = Union[Literal["redshift-data:statement-owner-iam-userid"]]

class aws_redshift_dataStatement(GenericResourceType[aws_redshift_data_privilege_type, aws_redshift_data_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    