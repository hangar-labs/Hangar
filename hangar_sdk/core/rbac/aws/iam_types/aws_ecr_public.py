from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ecr_public_privilege_type = Union[Literal["UntagResource"], Literal["UploadLayerPart"], Literal["GetAuthorizationToken"], Literal["GetRepositoryCatalogData"], Literal["InitiateLayerUpload"], Literal["PutRepositoryCatalogData"], Literal["CreateRepository"], Literal["BatchDeleteImage"], Literal["BatchCheckLayerAvailability"], Literal["ListTagsForResource"], Literal["DescribeRepositories"], Literal["PutRegistryCatalogData"], Literal["DescribeImages"], Literal["CompleteLayerUpload"], Literal["GetRegistryCatalogData"], Literal["GetRepositoryPolicy"], Literal["DescribeImageTags"], Literal["DescribeRegistries"], Literal["SetRepositoryPolicy"], Literal["TagResource"], Literal["DeleteRepository"], Literal["DeleteRepositoryPolicy"], Literal["PutImage"]]
aws_ecr_public_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ecr_publicStatement(GenericResourceType[aws_ecr_public_privilege_type, aws_ecr_public_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    