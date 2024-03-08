from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iottwinmaker_privilege_type = Union[Literal["ListWorkspaces"], Literal["DeleteSyncJob"], Literal["GetMetadataTransferJob"], Literal["ListScenes"], Literal["UntagResource"], Literal["ListSyncJobs"], Literal["CreateScene"], Literal["GetPropertyValueHistory"], Literal["CreateEntity"], Literal["CreateWorkspace"], Literal["UpdateComponentType"], Literal["ListEntities"], Literal["UpdatePricingPlan"], Literal["CreateSyncJob"], Literal["GetScene"], Literal["BatchPutPropertyValues"], Literal["ListMetadataTransferJobs"], Literal["GetPropertyValue"], Literal["ListTagsForResource"], Literal["CreateMetadataTransferJob"], Literal["GetPricingPlan"], Literal["GetWorkspace"], Literal["GetSyncJob"], Literal["CancelMetadataTransferJob"], Literal["DeleteScene"], Literal["GetComponentType"], Literal["GetEntity"], Literal["ExecuteQuery"], Literal["UpdateScene"], Literal["ListComponents"], Literal["UpdateEntity"], Literal["DeleteWorkspace"], Literal["CreateComponentType"], Literal["ListProperties"], Literal["DeleteComponentType"], Literal["ListComponentTypes"], Literal["TagResource"], Literal["ListSyncResources"], Literal["UpdateWorkspace"], Literal["DeleteEntity"]]
aws_iottwinmaker_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iottwinmakerStatement(GenericResourceType[aws_iottwinmaker_privilege_type, aws_iottwinmaker_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    