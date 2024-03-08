from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_s3_object_lambda_privilege_type = Union[Literal["DeleteObjectVersionTagging"], Literal["PutObjectVersionTagging"], Literal["WriteGetObjectResponse"], Literal["DeleteObjectVersion"], Literal["PutObjectRetention"], Literal["PutObjectAcl"], Literal["PutObject"], Literal["AbortMultipartUpload"], Literal["DeleteObject"], Literal["ListBucketVersions"], Literal["PutObjectVersionAcl"], Literal["GetObjectVersionAcl"], Literal["PutObjectTagging"], Literal["GetObjectTagging"], Literal["GetObjectAcl"], Literal["GetObjectRetention"], Literal["ListMultipartUploadParts"], Literal["DeleteObjectTagging"], Literal["GetObjectLegalHold"], Literal["GetObject"], Literal["GetObjectVersion"], Literal["ListBucketMultipartUploads"], Literal["RestoreObject"], Literal["ListBucket"], Literal["PutObjectLegalHold"], Literal["GetObjectVersionTagging"]]
aws_s3_object_lambda_condition_type = Union[Literal["s3-object-lambda:signatureAge"], Literal["s3-object-lambda:versionid"], Literal["s3-object-lambda:authType"], Literal["s3-object-lambda:TlsVersion"]]

class aws_s3_object_lambdaStatement(GenericResourceType[aws_s3_object_lambda_privilege_type, aws_s3_object_lambda_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    