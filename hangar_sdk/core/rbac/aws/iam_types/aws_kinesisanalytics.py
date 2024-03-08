from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_kinesisanalytics_privilege_type = Union[Literal["DescribeApplicationSnapshot"], Literal["UntagResource"], Literal["DescribeApplication"], Literal["AddApplicationReferenceDataSource"], Literal["AddApplicationInputProcessingConfiguration"], Literal["CreateApplication"], Literal["ListApplicationSnapshots"], Literal["ListApplicationVersions"], Literal["UpdateApplication"], Literal["DeleteApplicationInputProcessingConfiguration"], Literal["ListTagsForResource"], Literal["DeleteApplicationVpcConfiguration"], Literal["AddApplicationVpcConfiguration"], Literal["DeleteApplication"], Literal["CreateApplicationSnapshot"], Literal["ListApplications"], Literal["DeleteApplicationSnapshot"], Literal["UpdateApplicationMaintenanceConfiguration"], Literal["AddApplicationOutput"], Literal["GetApplicationState"], Literal["DiscoverInputSchema"], Literal["StopApplication"], Literal["TagResource"], Literal["DeleteApplicationCloudWatchLoggingOption"], Literal["AddApplicationInput"], Literal["AddApplicationCloudWatchLoggingOption"], Literal["CreateApplicationPresignedUrl"], Literal["StartApplication"], Literal["DeleteApplicationReferenceDataSource"], Literal["RollbackApplication"], Literal["DeleteApplicationOutput"], Literal["DescribeApplicationVersion"]]
aws_kinesisanalytics_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_kinesisanalyticsStatement(GenericResourceType[aws_kinesisanalytics_privilege_type, aws_kinesisanalytics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    