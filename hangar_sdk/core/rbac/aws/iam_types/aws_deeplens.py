from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_deeplens_privilege_type = Union[Literal["GetAssociatedResources"], Literal["CreateProject"], Literal["DeployProject"], Literal["BatchGetProject"], Literal["GetModel"], Literal["RemoveProject"], Literal["RegisterDevice"], Literal["CreateModel"], Literal["AssociateServiceRoleToAccount"], Literal["ListDevices"], Literal["CreateDeviceCertificates"], Literal["GetDevice"], Literal["BatchGetModel"], Literal["ListProjects"], Literal["GetDeploymentStatus"], Literal["BatchGetDevice"], Literal["DeregisterDevice"], Literal["ImportProjectFromTemplate"], Literal["UpdateProject"], Literal["DeleteModel"], Literal["DeleteProject"], Literal["GetProject"], Literal["ListModels"], Literal["ListDeployments"]]
aws_deeplens_condition_type = None

class aws_deeplensStatement(GenericResourceType[aws_deeplens_privilege_type, aws_deeplens_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    