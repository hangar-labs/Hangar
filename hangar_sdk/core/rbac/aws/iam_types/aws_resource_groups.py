from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_resource_groups_privilege_type = Union[Literal["PutGroupConfiguration"], Literal["UpdateGroup"], Literal["ListGroupResources"], Literal["UpdateGroupQuery"], Literal["GetGroup"], Literal["GroupResources"], Literal["CreateGroup"], Literal["SearchResources"], Literal["Tag"], Literal["GetAccountSettings"], Literal["Untag"], Literal["ListGroups"], Literal["GetGroupConfiguration"], Literal["UngroupResources"], Literal["DeleteGroup"], Literal["DisassociateResource"], Literal["GetTags"], Literal["GetGroupQuery"], Literal["PutGroupPolicy"], Literal["UpdateAccountSettings"], Literal["AssociateResource"]]
aws_resource_groups_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_resource_groupsStatement(GenericResourceType[aws_resource_groups_privilege_type, aws_resource_groups_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    