from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_thinclient_privilege_type = Union[Literal["ListTagsForResource"], Literal["DeregisterDevice"], Literal["UntagResource"], Literal["UpdateEnvironment"], Literal["ListEnvironments"], Literal["ListDevices"], Literal["ListDeviceSessions"], Literal["ListSoftwareSets"], Literal["TagResource"], Literal["GetDevice"], Literal["UpdateDevice"], Literal["GetEnvironment"], Literal["DeleteEnvironment"], Literal["CreateEnvironment"], Literal["GetSoftwareSet"], Literal["DeleteDevice"], Literal["UpdateSoftwareSet"]]
aws_thinclient_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_thinclientStatement(GenericResourceType[aws_thinclient_privilege_type, aws_thinclient_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    