from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_oam_privilege_type = Union[Literal["GetLink"], Literal["ListTagsForResource"], Literal["PutSinkPolicy"], Literal["UpdateLink"], Literal["ListAttachedLinks"], Literal["GetSink"], Literal["UntagResource"], Literal["DeleteLink"], Literal["ListLinks"], Literal["TagResource"], Literal["CreateSink"], Literal["ListSinks"], Literal["GetSinkPolicy"], Literal["DeleteSink"], Literal["CreateLink"]]
aws_oam_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["oam:ResourceTypes"], Literal["aws:RequestTag/${TagKey}"]]

class aws_oamStatement(GenericResourceType[aws_oam_privilege_type, aws_oam_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    