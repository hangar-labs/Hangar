from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_signer_privilege_type = Union[Literal["UntagResource"], Literal["GetSigningPlatform"], Literal["DescribeSigningJob"], Literal["ListSigningProfiles"], Literal["GetSigningProfile"], Literal["ListTagsForResource"], Literal["GetRevocationStatus"], Literal["ListSigningJobs"], Literal["RevokeSignature"], Literal["AddProfilePermission"], Literal["RemoveProfilePermission"], Literal["SignPayload"], Literal["StartSigningJob"], Literal["TagResource"], Literal["RevokeSigningProfile"], Literal["ListSigningPlatforms"], Literal["PutSigningProfile"], Literal["ListProfilePermissions"], Literal["CancelSigningProfile"]]
aws_signer_condition_type = Union[Literal["aws:TagKeys"], Literal["signer:ProfileVersion"], Literal["aws:RequestTag/${TagKey}"]]

class aws_signerStatement(GenericResourceType[aws_signer_privilege_type, aws_signer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    