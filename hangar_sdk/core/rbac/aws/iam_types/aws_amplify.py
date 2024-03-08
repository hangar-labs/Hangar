from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_amplify_privilege_type = Union[Literal["CreateWebHook"], Literal["UpdateWebHook"], Literal["UntagResource"], Literal["GetBranch"], Literal["GetDomainAssociation"], Literal["ListArtifacts"], Literal["DeleteJob"], Literal["StartJob"], Literal["DeleteBranch"], Literal["DeleteWebHook"], Literal["ListBranches"], Literal["DeleteDomainAssociation"], Literal["CreateDeployment"], Literal["ListApps"], Literal["ListBackendEnvironments"], Literal["CreateDomainAssociation"], Literal["DeleteApp"], Literal["GetBackendEnvironment"], Literal["CreateApp"], Literal["ListTagsForResource"], Literal["UpdateDomainAssociation"], Literal["UpdateBranch"], Literal["StartDeployment"], Literal["UpdateApp"], Literal["DeleteBackendEnvironment"], Literal["GenerateAccessLogs"], Literal["GetApp"], Literal["GetArtifactUrl"], Literal["GetWebHook"], Literal["StopJob"], Literal["ListJobs"], Literal["ListWebHooks"], Literal["TagResource"], Literal["CreateBackendEnvironment"], Literal["ListDomainAssociations"], Literal["GetJob"], Literal["CreateBranch"]]
aws_amplify_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_amplifyStatement(GenericResourceType[aws_amplify_privilege_type, aws_amplify_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    