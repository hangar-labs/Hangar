from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codeguru_reviewer_privilege_type = Union[Literal["AssociateRepository"], Literal["ListRecommendations"], Literal["CreateConnectionToken"], Literal["DisassociateRepository"], Literal["GetMetricsData"], Literal["UnTagResource"], Literal["ListCodeReviews"], Literal["DescribeRecommendationFeedback"], Literal["DescribeCodeReview"], Literal["ListRepositoryAssociations"], Literal["TagResource"], Literal["DescribeRepositoryAssociation"], Literal["ListRecommendationFeedback"], Literal["ListTagsForResource"], Literal["CreateCodeReview"], Literal["PutRecommendationFeedback"], Literal["ListThirdPartyRepositories"]]
aws_codeguru_reviewer_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codeguru_reviewerStatement(GenericResourceType[aws_codeguru_reviewer_privilege_type, aws_codeguru_reviewer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    