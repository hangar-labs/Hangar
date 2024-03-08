from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mediaconvert_privilege_type = Union[Literal["DeletePolicy"], Literal["DeleteQueue"], Literal["DeleteJobTemplate"], Literal["UpdateJobTemplate"], Literal["UntagResource"], Literal["DisassociateCertificate"], Literal["PutPolicy"], Literal["ListPresets"], Literal["GetJobTemplate"], Literal["DeletePreset"], Literal["GetQueue"], Literal["UpdateQueue"], Literal["ListTagsForResource"], Literal["ListJobTemplates"], Literal["GetPreset"], Literal["DescribeEndpoints"], Literal["CreateJob"], Literal["UpdatePreset"], Literal["GetPolicy"], Literal["ListQueues"], Literal["CreateQueue"], Literal["CreatePreset"], Literal["CancelJob"], Literal["CreateJobTemplate"], Literal["ListJobs"], Literal["TagResource"], Literal["AssociateCertificate"], Literal["GetJob"]]
aws_mediaconvert_condition_type = Union[Literal["aws:TagKeys"], Literal["mediaconvert:HttpInputsAllowed"], Literal["mediaconvert:S3InputsAllowed"], Literal["mediaconvert:HttpsInputsAllowed"], Literal["aws:RequestTag/${TagKey}"]]

class aws_mediaconvertStatement(GenericResourceType[aws_mediaconvert_privilege_type, aws_mediaconvert_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    