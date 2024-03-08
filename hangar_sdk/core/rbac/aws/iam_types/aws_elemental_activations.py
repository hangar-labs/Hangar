from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_elemental_activations_privilege_type = Union[Literal["ListTagsForResource"], Literal["GetActivation"], Literal["UntagResource"], Literal["StartFileUpload"], Literal["StartAccountRegistration"], Literal["CompleteFileUpload"], Literal["GenerateLicenses"], Literal["TagResource"], Literal["CompleteAccountRegistration"], Literal["DownloadSoftware"]]
aws_elemental_activations_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_elemental_activationsStatement(GenericResourceType[aws_elemental_activations_privilege_type, aws_elemental_activations_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    