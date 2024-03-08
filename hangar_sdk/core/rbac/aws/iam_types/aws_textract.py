from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_textract_privilege_type = Union[Literal["GetAdapterVersion"], Literal["GetExpenseAnalysis"], Literal["UpdateAdapter"], Literal["UntagResource"], Literal["AnalyzeExpense"], Literal["GetAdapter"], Literal["ListAdapters"], Literal["StartDocumentTextDetection"], Literal["DeleteAdapterVersion"], Literal["CreateAdapter"], Literal["AnalyzeDocument"], Literal["ListTagsForResource"], Literal["ListAdapterVersions"], Literal["AnalyzeID"], Literal["StartLendingAnalysis"], Literal["CreateAdapterVersion"], Literal["GetDocumentAnalysis"], Literal["DeleteAdapter"], Literal["GetLendingAnalysisSummary"], Literal["StartDocumentAnalysis"], Literal["StartExpenseAnalysis"], Literal["GetDocumentTextDetection"], Literal["TagResource"], Literal["DetectDocumentText"], Literal["GetLendingAnalysis"]]
aws_textract_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_textractStatement(GenericResourceType[aws_textract_privilege_type, aws_textract_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    