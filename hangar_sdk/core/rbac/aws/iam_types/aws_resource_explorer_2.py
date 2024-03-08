from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_resource_explorer_2_privilege_type = Union[Literal["UntagResource"], Literal["AssociateDefaultView"], Literal["ListViews"], Literal["Search"], Literal["CreateIndex"], Literal["ListIndexes"], Literal["ListSupportedResourceTypes"], Literal["UpdateView"], Literal["ListTagsForResource"], Literal["GetDefaultView"], Literal["GetView"], Literal["DisassociateDefaultView"], Literal["GetIndex"], Literal["CreateView"], Literal["BatchGetView"], Literal["GetAccountLevelServiceConfiguration"], Literal["DeleteView"], Literal["TagResource"], Literal["UpdateIndexType"], Literal["ListIndexesForMembers"], Literal["DeleteIndex"]]
aws_resource_explorer_2_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_resource_explorer_2Statement(GenericResourceType[aws_resource_explorer_2_privilege_type, aws_resource_explorer_2_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    