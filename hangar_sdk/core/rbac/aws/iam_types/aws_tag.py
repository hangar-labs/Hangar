from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_tag_privilege_type = Union[Literal["GetResources"], Literal["GetComplianceSummary"], Literal["StartReportCreation"], Literal["TagResources"], Literal["GetTagValues"], Literal["DescribeReportCreation"], Literal["UntagResources"], Literal["GetTagKeys"]]
aws_tag_condition_type = None

class aws_tagStatement(GenericResourceType[aws_tag_privilege_type, aws_tag_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    