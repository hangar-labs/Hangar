from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_healthlake_privilege_type = Union[Literal["UpdateResource"], Literal["UntagResource"], Literal["StartFHIRExportJob"], Literal["StartFHIRImportJob"], Literal["ListFHIRExportJobs"], Literal["ListFHIRImportJobs"], Literal["SearchWithGet"], Literal["SearchWithPost"], Literal["ListTagsForResource"], Literal["CreateFHIRDatastore"], Literal["ListFHIRDatastores"], Literal["DeleteFHIRDatastore"], Literal["DescribeFHIRExportJob"], Literal["GetCapabilities"], Literal["DeleteResource"], Literal["CreateResource"], Literal["ReadResource"], Literal["DescribeFHIRImportJob"], Literal["TagResource"], Literal["DescribeFHIRDatastore"]]
aws_healthlake_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_healthlakeStatement(GenericResourceType[aws_healthlake_privilege_type, aws_healthlake_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    