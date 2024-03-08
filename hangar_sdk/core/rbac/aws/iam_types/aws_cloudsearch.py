from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudsearch_privilege_type = Union[Literal["RemoveTags"], Literal["IndexDocuments"], Literal["DescribeSuggesters"], Literal["ListTags"], Literal["BuildSuggesters"], Literal["DefineIndexField"], Literal["DescribeScalingParameters"], Literal["DefineExpression"], Literal["DefineSuggester"], Literal["DescribeServiceAccessPolicies"], Literal["ListDomainNames"], Literal["DefineAnalysisScheme"], Literal["UpdateDomainEndpointOptions"], Literal["DeleteSuggester"], Literal["DescribeAnalysisSchemes"], Literal["CreateDomain"], Literal["search"], Literal["DeleteAnalysisScheme"], Literal["suggest"], Literal["UpdateServiceAccessPolicies"], Literal["DescribeDomains"], Literal["DescribeExpressions"], Literal["AddTags"], Literal["DescribeAvailabilityOptions"], Literal["DescribeIndexFields"], Literal["UpdateAvailabilityOptions"], Literal["DeleteDomain"], Literal["document"], Literal["DeleteIndexField"], Literal["DescribeDomainEndpointOptions"], Literal["UpdateScalingParameters"], Literal["DeleteExpression"]]
aws_cloudsearch_condition_type = None

class aws_cloudsearchStatement(GenericResourceType[aws_cloudsearch_privilege_type, aws_cloudsearch_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    