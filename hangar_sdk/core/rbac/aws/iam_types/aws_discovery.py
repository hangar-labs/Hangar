from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_discovery_privilege_type = Union[Literal["ListConfigurations"], Literal["StartBatchDeleteConfigurationTask"], Literal["CreateTags"], Literal["StopDataCollectionByAgentIds"], Literal["StartDataCollectionByAgentIds"], Literal["DescribeTags"], Literal["StartExportTask"], Literal["DescribeAgents"], Literal["DescribeContinuousExports"], Literal["DeleteTags"], Literal["DescribeImportTasks"], Literal["CreateApplication"], Literal["DisassociateConfigurationItemsFromApplication"], Literal["UpdateApplication"], Literal["BatchDeleteImportData"], Literal["BatchDeleteAgents"], Literal["DescribeBatchDeleteConfigurationTask"], Literal["StartImportTask"], Literal["DeleteApplications"], Literal["GetDiscoverySummary"], Literal["AssociateConfigurationItemsToApplication"], Literal["StopContinuousExport"], Literal["StartContinuousExport"], Literal["ListServerNeighbors"], Literal["DescribeConfigurations"], Literal["ExportConfigurations"], Literal["DescribeExportTasks"], Literal["GetNetworkConnectionGraph"], Literal["DescribeExportConfigurations"]]
aws_discovery_condition_type = Union[Literal["aws:TagKeys"]]

class aws_discoveryStatement(GenericResourceType[aws_discovery_privilege_type, aws_discovery_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    