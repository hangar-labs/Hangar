from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_artifact_privilege_type = Union[Literal["AcceptAgreement"], Literal["GetReport"], Literal["PutAccountSettings"], Literal["GetTermForReport"], Literal["GetAccountSettings"], Literal["ListReports"], Literal["Get"], Literal["TerminateAgreement"], Literal["DownloadAgreement"], Literal["GetReportMetadata"]]
aws_artifact_condition_type = None

class aws_artifactStatement(GenericResourceType[aws_artifact_privilege_type, aws_artifact_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    