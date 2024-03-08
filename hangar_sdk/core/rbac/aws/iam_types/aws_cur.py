from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cur_privilege_type = Union[Literal["GetClassicReportPreferences"], Literal["DescribeReportDefinitions"], Literal["UntagResource"], Literal["DeleteReportDefinition"], Literal["TagResource"], Literal["PutReportDefinition"], Literal["PutClassicReportPreferences"], Literal["ValidateReportDestination"], Literal["ListTagsForResource"], Literal["ModifyReportDefinition"], Literal["GetUsageReport"], Literal["GetClassicReport"]]
aws_cur_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_curStatement(GenericResourceType[aws_cur_privilege_type, aws_cur_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    