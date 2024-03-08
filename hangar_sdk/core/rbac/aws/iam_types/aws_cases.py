from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cases_privilege_type = Union[Literal["ListDomains"], Literal["SearchRelatedItems"], Literal["UntagResource"], Literal["ListLayouts"], Literal["CreateTemplate"], Literal["CreateRelatedItem"], Literal["CreateLayout"], Literal["CreateField"], Literal["GetTemplate"], Literal["ListFields"], Literal["ListFieldOptions"], Literal["BatchGetField"], Literal["PutCaseEventConfiguration"], Literal["CreateDomain"], Literal["ListTagsForResource"], Literal["GetCaseEventConfiguration"], Literal["GetDomain"], Literal["ListCasesForContact"], Literal["BatchPutFieldOptions"], Literal["GetCase"], Literal["UpdateLayout"], Literal["GetLayout"], Literal["UpdateTemplate"], Literal["CreateCase"], Literal["DeleteDomain"], Literal["SearchCases"], Literal["TagResource"], Literal["ListTemplates"], Literal["UpdateField"], Literal["UpdateCase"]]
aws_cases_condition_type = Union[Literal["connect:UserArn"], Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_casesStatement(GenericResourceType[aws_cases_privilege_type, aws_cases_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    