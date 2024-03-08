from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ec2_instance_connect_privilege_type = Union[Literal["SendSSHPublicKey"], Literal["OpenTunnel"], Literal["SendSerialConsoleSSHPublicKey"]]
aws_ec2_instance_connect_condition_type = Union[Literal["aws:ResourceTag/${TagKey}"], Literal["ec2:osuser"], Literal["ec2-instance-connect:privateIpAddress"], Literal["ec2-instance-connect:MaxTunnelDuration"], Literal["ec2:ResourceTag/${TagKey}"], Literal["ec2-instance-connect:remotePort"]]

class aws_ec2_instance_connectStatement(GenericResourceType[aws_ec2_instance_connect_privilege_type, aws_ec2_instance_connect_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    