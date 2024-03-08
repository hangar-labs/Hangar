from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_bcm_data_exports_privilege_type = Union[Literal["UpdateExport"], Literal["ListTables"], Literal["GetTable"], Literal["UntagResource"], Literal["CreateExport"], Literal["GetExport"], Literal["TagResource"], Literal["ListExecutions"], Literal["ListTagsForResource"], Literal["DeleteExport"], Literal["GetExecution"], Literal["ListExports"]]
aws_bcm_data_exports_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_bcm_data_exportsStatement(GenericResourceType[aws_bcm_data_exports_privilege_type, aws_bcm_data_exports_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    