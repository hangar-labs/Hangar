from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mobilehub_privilege_type = Union[Literal["CreateProject"], Literal["ImportProject"], Literal["ListAvailableFeatures"], Literal["CreateServiceRole"], Literal["DescribeBundle"], Literal["VerifyServiceRole"], Literal["ListProjectSnapshots"], Literal["DeleteProjectSnapshot"], Literal["ListProjects"], Literal["ValidateProject"], Literal["UpdateProject"], Literal["GetProjectSnapshot"], Literal["ListAvailableConnectors"], Literal["DeleteProject"], Literal["SynchronizeProject"], Literal["ExportProject"], Literal["GetProject"], Literal["GenerateProjectParameters"], Literal["ListAvailableRegions"], Literal["ListBundles"], Literal["DeployToStage"], Literal["ExportBundle"], Literal["InstallBundle"]]
aws_mobilehub_condition_type = None

class aws_mobilehubStatement(GenericResourceType[aws_mobilehub_privilege_type, aws_mobilehub_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    