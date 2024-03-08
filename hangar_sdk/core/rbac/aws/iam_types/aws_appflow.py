from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_appflow_privilege_type = Union[Literal["DescribeConnector"], Literal["RunFlow"], Literal["DescribeFlows"], Literal["UntagResource"], Literal["DescribeConnectorProfiles"], Literal["DescribeFlow"], Literal["UpdateConnectorProfile"], Literal["CreateConnectorProfile"], Literal["DeleteFlow"], Literal["ListConnectorFields"], Literal["DescribeConnectors"], Literal["UnRegisterConnector"], Literal["DescribeFlowExecution"], Literal["DescribeConnectorFields"], Literal["RegisterConnector"], Literal["ListTagsForResource"], Literal["DescribeConnectorEntity"], Literal["StopFlow"], Literal["DeleteConnectorProfile"], Literal["UseConnectorProfile"], Literal["StartFlow"], Literal["CancelFlowExecutions"], Literal["ListFlows"], Literal["DescribeFlowExecutionRecords"], Literal["ListConnectors"], Literal["ResetConnectorMetadataCache"], Literal["TagResource"], Literal["ListConnectorEntities"], Literal["UpdateConnectorRegistration"], Literal["CreateFlow"], Literal["UpdateFlow"]]
aws_appflow_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_appflowStatement(GenericResourceType[aws_appflow_privilege_type, aws_appflow_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    