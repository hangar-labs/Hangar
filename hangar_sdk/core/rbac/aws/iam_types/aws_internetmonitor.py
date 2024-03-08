from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_internetmonitor_privilege_type = Union[Literal["GetHealthEvent"], Literal["StartQuery"], Literal["ListHealthEvents"], Literal["UntagResource"], Literal["GetMonitor"], Literal["CreateMonitor"], Literal["ListMonitors"], Literal["TagResource"], Literal["GetQueryStatus"], Literal["DeleteMonitor"], Literal["StopQuery"], Literal["UpdateMonitor"], Literal["ListTagsForResource"], Literal["GetQueryResults"]]
aws_internetmonitor_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_internetmonitorStatement(GenericResourceType[aws_internetmonitor_privilege_type, aws_internetmonitor_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    