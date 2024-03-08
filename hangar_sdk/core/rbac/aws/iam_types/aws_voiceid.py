from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_voiceid_privilege_type = Union[Literal["DescribeDomain"], Literal["DescribeFraudster"], Literal["ListDomains"], Literal["RegisterComplianceConsent"], Literal["UntagResource"], Literal["DescribeComplianceConsent"], Literal["ListSpeakerEnrollmentJobs"], Literal["StartFraudsterRegistrationJob"], Literal["DescribeFraudsterRegistrationJob"], Literal["DeleteFraudster"], Literal["UpdateDomain"], Literal["OptOutSpeaker"], Literal["StartSpeakerEnrollmentJob"], Literal["CreateDomain"], Literal["ListTagsForResource"], Literal["ListFraudsters"], Literal["ListWatchlists"], Literal["DeleteSpeaker"], Literal["EvaluateSession"], Literal["ListSpeakers"], Literal["DeleteWatchlist"], Literal["DisassociateFraudster"], Literal["DescribeWatchlist"], Literal["AssociateFraudster"], Literal["DescribeSpeakerEnrollmentJob"], Literal["ListFraudsterRegistrationJobs"], Literal["UpdateWatchlist"], Literal["DeleteDomain"], Literal["TagResource"], Literal["CreateWatchlist"], Literal["DescribeSpeaker"]]
aws_voiceid_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_voiceidStatement(GenericResourceType[aws_voiceid_privilege_type, aws_voiceid_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    