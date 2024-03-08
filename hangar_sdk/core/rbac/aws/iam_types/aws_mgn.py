from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mgn_privilege_type = Union[Literal["DescribeSourceServers"], Literal["GetChannelCommandsForMgn"], Literal["DescribeReplicationConfigurationTemplates"], Literal["NotifyAgentConnectedForMgn"], Literal["CreateConnector"], Literal["DeleteJob"], Literal["SendAgentMetricsForMgn"], Literal["StartReplication"], Literal["UpdateReplicationConfiguration"], Literal["DescribeJobLogItems"], Literal["DescribeSnapshotRequestsForMgn"], Literal["StopReplication"], Literal["ListApplications"], Literal["StartCutover"], Literal["TagResource"], Literal["UpdateAgentReplicationInfoForMgn"], Literal["AssociateSourceServers"], Literal["RemoveTemplateAction"], Literal["UpdateWave"], Literal["DeleteReplicationConfigurationTemplate"], Literal["DescribeReplicationServerAssociationsForMgn"], Literal["UnarchiveWave"], Literal["ListExports"], Literal["ChangeServerLifeCycleState"], Literal["NotifyAgentAuthenticationForMgn"], Literal["GetAgentReplicationInfoForMgn"], Literal["RetryDataReplication"], Literal["StartImport"], Literal["UpdateAgentConversionInfoForMgn"], Literal["FinalizeCutover"], Literal["DeleteApplication"], Literal["InitializeService"], Literal["PutSourceServerAction"], Literal["ArchiveApplication"], Literal["ListImports"], Literal["PutTemplateAction"], Literal["UnarchiveApplication"], Literal["UpdateLaunchConfiguration"], Literal["RegisterAgentForMgn"], Literal["ListImportErrors"], Literal["SendClientMetricsForMgn"], Literal["ListExportErrors"], Literal["UpdateConnector"], Literal["MarkAsArchived"], Literal["SendVcenterClientMetricsForMgn"], Literal["RemoveSourceServerAction"], Literal["GetReplicationConfiguration"], Literal["UpdateAgentBacklogForMgn"], Literal["CreateVcenterClientForMgn"], Literal["ListSourceServerActions"], Literal["CreateApplication"], Literal["ListTemplateActions"], Literal["GetVcenterClientCommandsForMgn"], Literal["UpdateApplication"], Literal["CreateWave"], Literal["IssueClientCertificateForMgn"], Literal["DeleteSourceServer"], Literal["StartExport"], Literal["DeleteLaunchConfigurationTemplate"], Literal["NotifyVcenterClientStartedForMgn"], Literal["GetAgentRuntimeConfigurationForMgn"], Literal["UpdateReplicationConfigurationTemplate"], Literal["DescribeLaunchConfigurationTemplates"], Literal["GetAgentCommandForMgn"], Literal["UpdateAgentSourcePropertiesForMgn"], Literal["UpdateAgentReplicationProcessStateForMgn"], Literal["DeleteWave"], Literal["ListManagedAccounts"], Literal["ArchiveWave"], Literal["SendAgentLogsForMgn"], Literal["DisassociateApplications"], Literal["SendVcenterClientCommandResultForMgn"], Literal["UntagResource"], Literal["DisassociateSourceServers"], Literal["UpdateLaunchConfigurationTemplate"], Literal["StartTest"], Literal["ListWaves"], Literal["NotifyAgentDisconnectedForMgn"], Literal["GetLaunchConfiguration"], Literal["BatchCreateVolumeSnapshotGroupForMgn"], Literal["SendClientLogsForMgn"], Literal["VerifyClientRoleForMgn"], Literal["DescribeJobs"], Literal["CreateLaunchConfigurationTemplate"], Literal["DescribeVcenterClients"], Literal["GetAgentConfirmedResumeInfoForMgn"], Literal["ListTagsForResource"], Literal["DeleteVcenterClient"], Literal["CreateReplicationConfigurationTemplate"], Literal["SendChannelCommandResultForMgn"], Literal["BatchDeleteSnapshotRequestForMgn"], Literal["UpdateSourceServer"], Literal["DeleteConnector"], Literal["GetAgentInstallationAssetsForMgn"], Literal["AssociateApplications"], Literal["NotifyAgentReplicationProgressForMgn"], Literal["ListConnectors"], Literal["SendVcenterClientLogsForMgn"], Literal["ResumeReplication"], Literal["UpdateSourceServerReplicationType"], Literal["GetAgentSnapshotCreditsForMgn"], Literal["TerminateTargetInstances"], Literal["PauseReplication"], Literal["DisconnectFromService"]]
aws_mgn_condition_type = Union[Literal["aws:TagKeys"], Literal["mgn:CreateAction"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mgnStatement(GenericResourceType[aws_mgn_privilege_type, aws_mgn_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    