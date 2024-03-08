from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mgh_privilege_type = Union[Literal["ListApplicationStates"], Literal["AssociateCreatedArtifact"], Literal["AssociateDiscoveredResource"], Literal["NotifyApplicationState"], Literal["DisassociateCreatedArtifact"], Literal["CreateProgressUpdateStream"], Literal["ListDiscoveredResources"], Literal["ListCreatedArtifacts"], Literal["NotifyMigrationTaskState"], Literal["DescribeApplicationState"], Literal["DescribeMigrationTask"], Literal["PutResourceAttributes"], Literal["DeleteHomeRegionControl"], Literal["GetHomeRegion"], Literal["DescribeHomeRegionControls"], Literal["DeleteProgressUpdateStream"], Literal["ListProgressUpdateStreams"], Literal["CreateHomeRegionControl"], Literal["ImportMigrationTask"], Literal["DisassociateDiscoveredResource"], Literal["ListMigrationTasks"]]
aws_mgh_condition_type = None

class aws_mghStatement(GenericResourceType[aws_mgh_privilege_type, aws_mgh_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    