from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_medical_imaging_privilege_type = Union[Literal["DeleteImageSet"], Literal["UpdateImageSetMetadata"], Literal["SearchImageSets"], Literal["UntagResource"], Literal["CreateDatastore"], Literal["GetDICOMImportJob"], Literal["CopyImageSet"], Literal["GetImageSetMetadata"], Literal["ListImageSetVersions"], Literal["ListDICOMImportJobs"], Literal["GetImageSet"], Literal["StartDICOMImportJob"], Literal["GetImageFrame"], Literal["ListDatastores"], Literal["TagResource"], Literal["GetDatastore"], Literal["ListTagsForResource"], Literal["DeleteDatastore"]]
aws_medical_imaging_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_medical_imagingStatement(GenericResourceType[aws_medical_imaging_privilege_type, aws_medical_imaging_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    