from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_one_privilege_type = Union[Literal["GetDeviceInstanceConfiguration"], Literal["RebootDevice"], Literal["UntagResource"], Literal["UpdateDeviceConfigurationTemplate"], Literal["UpdateDeviceInstance"], Literal["GetSiteAddress"], Literal["ListUsers"], Literal["UpdateSiteAddress"], Literal["CreateDeviceInstance"], Literal["UpdateSite"], Literal["GetDeviceConfigurationTemplate"], Literal["ListDeviceConfigurationTemplates"], Literal["ListTagsForResource"], Literal["ListSites"], Literal["CreateDeviceInstanceConfiguration"], Literal["GetSite"], Literal["CreateSite"], Literal["CreateDeviceActivationQrCode"], Literal["TagResource"], Literal["DeleteDeviceInstance"], Literal["GetDeviceInstance"], Literal["DeleteSite"], Literal["CreateDeviceConfigurationTemplate"], Literal["ListDeviceInstances"], Literal["DeleteUser"], Literal["DeleteDeviceConfigurationTemplate"], Literal["DeleteAssociatedDevice"]]
aws_one_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_oneStatement(GenericResourceType[aws_one_privilege_type, aws_one_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    