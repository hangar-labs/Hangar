from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codeguru_security_privilege_type = Union[Literal["GetMetricsSummary"], Literal["ListScans"], Literal["UpdateAccountConfiguration"], Literal["UntagResource"], Literal["GetAccountConfiguration"], Literal["TagResource"], Literal["CreateScan"], Literal["CreateUploadUrl"], Literal["DeleteScansByCategory"], Literal["ListFindingsMetrics"], Literal["ListTagsForResource"], Literal["ListFindings"], Literal["GetScan"], Literal["GetFindings"], Literal["BatchGetFindings"]]
aws_codeguru_security_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codeguru_securityStatement(GenericResourceType[aws_codeguru_security_privilege_type, aws_codeguru_security_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    