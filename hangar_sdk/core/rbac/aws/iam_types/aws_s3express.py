from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_s3express_privilege_type = Union[Literal["CreateBucket"], Literal["DeleteBucketPolicy"], Literal["ListAllMyDirectoryBuckets"], Literal["DeleteBucket"], Literal["PutBucketPolicy"], Literal["CreateSession"], Literal["GetBucketPolicy"]]
aws_s3express_condition_type = Union[Literal["s3express:signatureAge"], Literal["s3express:LocationName"], Literal["s3express:TlsVersion"], Literal["s3express:authType"], Literal["s3express:SessionMode"], Literal["s3express:ResourceAccount"], Literal["s3express:x-amz-content-sha256"], Literal["s3express:signatureversion"]]

class aws_s3expressStatement(GenericResourceType[aws_s3express_privilege_type, aws_s3express_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    