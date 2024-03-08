from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_serverlessrepo_privilege_type = Union[Literal["CreateApplicationVersion"], Literal["UnshareApplication"], Literal["CreateCloudFormationChangeSet"], Literal["GetApplication"], Literal["CreateApplication"], Literal["CreateCloudFormationTemplate"], Literal["GetApplicationPolicy"], Literal["ListApplicationDependencies"], Literal["DeleteApplication"], Literal["ListApplicationVersions"], Literal["SearchApplications"], Literal["UpdateApplication"], Literal["ListApplications"], Literal["GetCloudFormationTemplate"], Literal["PutApplicationPolicy"]]
aws_serverlessrepo_condition_type = Union[Literal["serverlessrepo:applicationType"]]

class aws_serverlessrepoStatement(GenericResourceType[aws_serverlessrepo_privilege_type, aws_serverlessrepo_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    