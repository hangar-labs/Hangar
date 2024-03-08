from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotanalytics_privilege_type = Union[Literal["StartPipelineReprocessing"], Literal["UntagResource"], Literal["UpdateChannel"], Literal["ListDatastores"], Literal["DescribeDataset"], Literal["DescribeLoggingOptions"], Literal["CreateChannel"], Literal["DeleteDatasetContent"], Literal["CreatePipeline"], Literal["ListDatasetContents"], Literal["DescribeDatastore"], Literal["ListChannels"], Literal["CreateDataset"], Literal["CreateDatasetContent"], Literal["DeleteDatastore"], Literal["ListTagsForResource"], Literal["CancelPipelineReprocessing"], Literal["DescribePipeline"], Literal["DeletePipeline"], Literal["UpdateDataset"], Literal["CreateDatastore"], Literal["UpdatePipeline"], Literal["BatchPutMessage"], Literal["UpdateDatastore"], Literal["SampleChannelData"], Literal["ListDatasets"], Literal["TagResource"], Literal["DeleteDataset"], Literal["GetDatasetContent"], Literal["DeleteChannel"], Literal["ListPipelines"], Literal["PutLoggingOptions"], Literal["DescribeChannel"], Literal["RunPipelineActivity"]]
aws_iotanalytics_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iotanalyticsStatement(GenericResourceType[aws_iotanalytics_privilege_type, aws_iotanalytics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    