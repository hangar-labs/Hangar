from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_amplifybackend_privilege_type = Union[Literal["UpdateBackendConfig"], Literal["ListS3Buckets"], Literal["UpdateBackendJob"], Literal["CreateBackendConfig"], Literal["UpdateBackendAPI"], Literal["CreateBackend"], Literal["CreateBackendAPI"], Literal["GetBackendAPIModels"], Literal["ImportBackendStorage"], Literal["GetBackendJob"], Literal["RemoveBackendConfig"], Literal["DeleteBackendAPI"], Literal["GetBackendAPI"], Literal["CloneBackend"], Literal["UpdateBackendStorage"], Literal["UpdateBackendAuth"], Literal["DeleteBackendStorage"], Literal["GenerateBackendAPIModels"], Literal["DeleteBackendAuth"], Literal["GetBackend"], Literal["DeleteToken"], Literal["GetBackendStorage"], Literal["CreateToken"], Literal["ListBackendJobs"], Literal["ImportBackendAuth"], Literal["DeleteBackend"], Literal["GetToken"], Literal["RemoveAllBackends"], Literal["GetBackendAuth"], Literal["CreateBackendAuth"], Literal["CreateBackendStorage"]]
aws_amplifybackend_condition_type = None

class aws_amplifybackendStatement(GenericResourceType[aws_amplifybackend_privilege_type, aws_amplifybackend_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    