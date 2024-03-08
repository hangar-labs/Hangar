from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_simspaceweaver_privilege_type = Union[Literal["StartClock"], Literal["ListSimulations"], Literal["DeleteSimulation"], Literal["ListApps"], Literal["StopApp"], Literal["StopSimulation"], Literal["CreateSnapshot"], Literal["DeleteApp"], Literal["DescribeApp"], Literal["StartSimulation"], Literal["UntagResource"], Literal["TagResource"], Literal["DescribeSimulation"], Literal["StartApp"], Literal["ListTagsForResource"], Literal["StopClock"]]
aws_simspaceweaver_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_simspaceweaverStatement(GenericResourceType[aws_simspaceweaver_privilege_type, aws_simspaceweaver_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    