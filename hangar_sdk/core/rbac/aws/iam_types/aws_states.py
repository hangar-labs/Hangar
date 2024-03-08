from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_states_privilege_type = Union[Literal["DescribeMapRun"], Literal["UpdateMapRun"], Literal["CreateActivity"], Literal["UntagResource"], Literal["ListStateMachines"], Literal["SendTaskFailure"], Literal["DescribeActivity"], Literal["SendTaskHeartbeat"], Literal["UpdateStateMachine"], Literal["UpdateStateMachineAlias"], Literal["ListStateMachineAliases"], Literal["DeleteStateMachine"], Literal["StartSyncExecution"], Literal["ListStateMachineVersions"], Literal["ListTagsForResource"], Literal["RedriveExecution"], Literal["ListActivities"], Literal["DescribeStateMachineAlias"], Literal["RevealSecrets"], Literal["CreateStateMachine"], Literal["DeleteActivity"], Literal["ListMapRuns"], Literal["DescribeExecution"], Literal["StopExecution"], Literal["ListExecutions"], Literal["DescribeStateMachineForExecution"], Literal["DescribeStateMachine"], Literal["DeleteStateMachineVersion"], Literal["SendTaskSuccess"], Literal["PublishStateMachineVersion"], Literal["DeleteStateMachineAlias"], Literal["StartExecution"], Literal["TestState"], Literal["GetActivityTask"], Literal["TagResource"], Literal["GetExecutionHistory"], Literal["CreateStateMachineAlias"], Literal["InvokeHTTPEndpoint"]]
aws_states_condition_type = Union[Literal["aws:TagKeys"], Literal["states:StateMachineQualifier"], Literal["aws:RequestTag/${TagKey}"]]

class aws_statesStatement(GenericResourceType[aws_states_privilege_type, aws_states_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    