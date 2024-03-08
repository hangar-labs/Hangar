from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_gamesparks_privilege_type = Union[Literal["ListExtensionVersions"], Literal["ListStageDeployments"], Literal["GetExtensionVersion"], Literal["UntagResource"], Literal["DeleteGame"], Literal["CreateGame"], Literal["GetExtension"], Literal["ListExtensions"], Literal["GetPlayerConnectionStatus"], Literal["GetSnapshot"], Literal["CreateSnapshot"], Literal["GetStage"], Literal["UpdateSnapshot"], Literal["StartGeneratedCodeJob"], Literal["ListTagsForResource"], Literal["InvokeBackend"], Literal["StartStageDeployment"], Literal["ListGames"], Literal["UpdateGameConfiguration"], Literal["DisconnectPlayer"], Literal["ListSnapshots"], Literal["ImportGameConfiguration"], Literal["UpdateStage"], Literal["ListStages"], Literal["DeleteStage"], Literal["GetGeneratedCodeJob"], Literal["GetStageDeployment"], Literal["ListGeneratedCodeJobs"], Literal["ExportSnapshot"], Literal["GetGameConfiguration"], Literal["CreateStage"], Literal["TagResource"], Literal["UpdateGame"], Literal["GetGame"]]
aws_gamesparks_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_gamesparksStatement(GenericResourceType[aws_gamesparks_privilege_type, aws_gamesparks_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    