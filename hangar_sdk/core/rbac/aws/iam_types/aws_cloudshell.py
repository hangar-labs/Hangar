from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudshell_privilege_type = Union[Literal["GetFileUploadUrls"], Literal["StopEnvironment"], Literal["GetEnvironmentStatus"], Literal["GetFileDownloadUrls"], Literal["DeleteEnvironment"], Literal["CreateEnvironment"], Literal["StartEnvironment"], Literal["CreateSession"], Literal["PutCredentials"]]
aws_cloudshell_condition_type = None

class aws_cloudshellStatement(GenericResourceType[aws_cloudshell_privilege_type, aws_cloudshell_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    