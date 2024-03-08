from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_timestream_privilege_type = Union[Literal["UntagResource"], Literal["ListScheduledQueries"], Literal["DeleteScheduledQuery"], Literal["Unload"], Literal["ListTables"], Literal["CreateDatabase"], Literal["UpdateDatabase"], Literal["DescribeBatchLoadTask"], Literal["DescribeScheduledQuery"], Literal["UpdateScheduledQuery"], Literal["DescribeTable"], Literal["ListMeasures"], Literal["ListTagsForResource"], Literal["ListDatabases"], Literal["Select"], Literal["DescribeEndpoints"], Literal["DescribeDatabase"], Literal["UpdateTable"], Literal["StartAwsBackupJob"], Literal["ExecuteScheduledQuery"], Literal["CreateScheduledQuery"], Literal["GetAwsRestoreStatus"], Literal["CreateTable"], Literal["StartAwsRestoreJob"], Literal["GetAwsBackupStatus"], Literal["ListBatchLoadTasks"], Literal["DeleteTable"], Literal["SelectValues"], Literal["CancelQuery"], Literal["PrepareQuery"], Literal["CreateBatchLoadTask"], Literal["TagResource"], Literal["DeleteDatabase"], Literal["ResumeBatchLoadTask"], Literal["WriteRecords"]]
aws_timestream_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_timestreamStatement(GenericResourceType[aws_timestream_privilege_type, aws_timestream_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    