from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ebs_privilege_type = Union[Literal["ListChangedBlocks"], Literal["PutSnapshotBlock"], Literal["GetSnapshotBlock"], Literal["CompleteSnapshot"], Literal["ListSnapshotBlocks"], Literal["StartSnapshot"]]
aws_ebs_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["ebs:VolumeSize"], Literal["ebs:Description"], Literal["ebs:ParentSnapshot"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ebsStatement(GenericResourceType[aws_ebs_privilege_type, aws_ebs_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    