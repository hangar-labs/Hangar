from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_amplifyuibuilder_privilege_type = Union[Literal["UpdateForm"], Literal["RefreshToken"], Literal["GetComponent"], Literal["DeleteTheme"], Literal["ListThemes"], Literal["ExchangeCodeForToken"], Literal["ListForms"], Literal["CreateForm"], Literal["PutMetadataFlag"], Literal["DeleteForm"], Literal["DeleteComponent"], Literal["GetCodegenJob"], Literal["GetTheme"], Literal["GetMetadata"], Literal["CreateTheme"], Literal["UpdateTheme"], Literal["ExportComponents"], Literal["ResetMetadataFlag"], Literal["ListComponents"], Literal["CreateComponent"], Literal["ListCodegenJobs"], Literal["ExportThemes"], Literal["UpdateComponent"], Literal["GetForm"], Literal["ExportForms"], Literal["StartCodegenJob"]]
aws_amplifyuibuilder_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_amplifyuibuilderStatement(GenericResourceType[aws_amplifyuibuilder_privilege_type, aws_amplifyuibuilder_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    