from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_networkmonitor_privilege_type = Union[Literal["UntagResource"], Literal["UpdateProbe"], Literal["GetMonitor"], Literal["CreateMonitor"], Literal["CreateProbe"], Literal["DeleteProbe"], Literal["ListMonitors"], Literal["DeleteMonitor"], Literal["TagResource"], Literal["UpdateMonitor"], Literal["GetProbe"], Literal["ListTagsForResource"]]
aws_networkmonitor_condition_type = Union[Literal["aws:TagKeys"]]

class aws_networkmonitorStatement(GenericResourceType[aws_networkmonitor_privilege_type, aws_networkmonitor_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    