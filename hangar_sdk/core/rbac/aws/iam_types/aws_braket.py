from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_braket_privilege_type = Union[Literal["CancelQuantumTask"], Literal["CancelJob"], Literal["CreateJob"], Literal["UntagResource"], Literal["AcceptUserAgreement"], Literal["GetUserAgreementStatus"], Literal["SearchJobs"], Literal["SearchQuantumTasks"], Literal["TagResource"], Literal["GetDevice"], Literal["GetServiceLinkedRoleStatus"], Literal["ListTagsForResource"], Literal["CreateQuantumTask"], Literal["AccessBraketFeature"], Literal["SearchDevices"], Literal["GetJob"], Literal["GetQuantumTask"]]
aws_braket_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_braketStatement(GenericResourceType[aws_braket_privilege_type, aws_braket_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    