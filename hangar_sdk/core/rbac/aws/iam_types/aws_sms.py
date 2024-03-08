from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sms_privilege_type = Union[Literal["DeleteAppReplicationConfiguration"], Literal["GetReplicationJobs"], Literal["StopAppReplication"], Literal["DisassociateConnector"], Literal["UpdateReplicationJob"], Literal["StartAppReplication"], Literal["GetConnectors"], Literal["DeleteAppValidationConfiguration"], Literal["DeleteServerCatalog"], Literal["SendMessage"], Literal["GetAppValidationOutput"], Literal["ListApps"], Literal["PutAppLaunchConfiguration"], Literal["TerminateApp"], Literal["DeleteApp"], Literal["ImportServerCatalog"], Literal["StartOnDemandAppReplication"], Literal["CreateApp"], Literal["GetMessages"], Literal["NotifyAppValidationOutput"], Literal["GetAppReplicationConfiguration"], Literal["LaunchApp"], Literal["PutAppValidationConfiguration"], Literal["PutAppReplicationConfiguration"], Literal["DeleteAppLaunchConfiguration"], Literal["UpdateApp"], Literal["GenerateChangeSet"], Literal["GetApp"], Literal["ImportAppCatalog"], Literal["GenerateTemplate"], Literal["GetAppLaunchConfiguration"], Literal["CreateReplicationJob"], Literal["StartOnDemandReplicationRun"], Literal["GetAppValidationConfiguration"], Literal["DeleteReplicationJob"], Literal["GetServers"], Literal["GetReplicationRuns"]]
aws_sms_condition_type = None

class aws_smsStatement(GenericResourceType[aws_sms_privilege_type, aws_sms_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    