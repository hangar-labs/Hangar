from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_importexport_privilege_type = Union[Literal["CancelJob"], Literal["CreateJob"], Literal["GetStatus"], Literal["ListJobs"], Literal["GetShippingLabel"], Literal["UpdateJob"]]
aws_importexport_condition_type = None

class aws_importexportStatement(GenericResourceType[aws_importexport_privilege_type, aws_importexport_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    