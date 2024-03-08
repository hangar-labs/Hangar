from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloud9_privilege_type = Union[Literal["DescribeEnvironmentMemberships"], Literal["UntagResource"], Literal["ListEnvironments"], Literal["UpdateSSHRemote"], Literal["CreateEnvironmentEC2"], Literal["GetMigrationExperiences"], Literal["DeleteEnvironment"], Literal["CreateEnvironmentSSH"], Literal["DeleteEnvironmentMembership"], Literal["DescribeEC2Remote"], Literal["GetUserPublicKey"], Literal["GetUserSettings"], Literal["ActivateEC2Remote"], Literal["CreateEnvironmentToken"], Literal["ListTagsForResource"], Literal["UpdateUserSettings"], Literal["DescribeEnvironmentStatus"], Literal["DescribeSSHRemote"], Literal["GetEnvironmentConfig"], Literal["UpdateEnvironment"], Literal["UpdateMembershipSettings"], Literal["CreateEnvironmentMembership"], Literal["ModifyTemporaryCredentialsOnEnvironmentEC2"], Literal["GetMembershipSettings"], Literal["UpdateEnvironmentSettings"], Literal["ValidateEnvironmentName"], Literal["TagResource"], Literal["UpdateEnvironmentMembership"], Literal["DescribeEnvironments"], Literal["GetEnvironmentSettings"]]
aws_cloud9_condition_type = Union[Literal["cloud9:EnvironmentName"], Literal["aws:TagKeys"], Literal["cloud9:EnvironmentId"], Literal["cloud9:InstanceType"], Literal["cloud9:SubnetId"], Literal["cloud9:UserArn"], Literal["cloud9:Permissions"], Literal["cloud9:OwnerArn"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cloud9Statement(GenericResourceType[aws_cloud9_privilege_type, aws_cloud9_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    