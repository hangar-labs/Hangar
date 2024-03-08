from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_identitystore_privilege_type = Union[Literal["UpdateGroup"], Literal["CreateGroupMembership"], Literal["CreateUser"], Literal["ListUsers"], Literal["CreateGroup"], Literal["GetGroupId"], Literal["ListGroupMembershipsForMember"], Literal["GetGroupMembershipId"], Literal["ListGroupMemberships"], Literal["GetUserId"], Literal["ListGroups"], Literal["DescribeUser"], Literal["DescribeGroupMembership"], Literal["DescribeGroup"], Literal["IsMemberInGroups"], Literal["DeleteGroup"], Literal["DeleteGroupMembership"], Literal["UpdateUser"], Literal["DeleteUser"]]
aws_identitystore_condition_type = None

class aws_identitystoreStatement(GenericResourceType[aws_identitystore_privilege_type, aws_identitystore_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    