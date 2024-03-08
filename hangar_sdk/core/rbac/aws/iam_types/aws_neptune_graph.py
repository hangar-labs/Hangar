from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_neptune_graph_privilege_type = Union[Literal["DeleteDataViaQuery"], Literal["ListImportTasks"], Literal["ListQueries"], Literal["UpdateGraph"], Literal["UntagResource"], Literal["GetGraphSummary"], Literal["DeletePrivateGraphEndpoint"], Literal["GetQueryStatus"], Literal["DeleteGraph"], Literal["GetImportTask"], Literal["GetStatisticsStatus"], Literal["RestoreGraphFromSnapshot"], Literal["GetPrivateGraphEndpoint"], Literal["CreateGraph"], Literal["GetGraph"], Literal["ListTagsForResource"], Literal["DeleteGraphSnapshot"], Literal["ResetGraph"], Literal["CreateGraphUsingImportTask"], Literal["GetEngineStatus"], Literal["CancelImportTask"], Literal["GetGraphSnapshot"], Literal["ReadDataViaQuery"], Literal["CancelQuery"], Literal["ListPrivateGraphEndpoints"], Literal["TagResource"], Literal["ListGraphSnapshots"], Literal["WriteDataViaQuery"], Literal["ListGraphs"], Literal["CreatePrivateGraphEndpoint"], Literal["CreateGraphSnapshot"]]
aws_neptune_graph_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_neptune_graphStatement(GenericResourceType[aws_neptune_graph_privilege_type, aws_neptune_graph_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    