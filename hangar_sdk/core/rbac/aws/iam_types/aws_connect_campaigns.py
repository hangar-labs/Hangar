from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_connect_campaigns_privilege_type = Union[Literal["UntagResource"], Literal["CreateCampaign"], Literal["StartCampaign"], Literal["DeleteInstanceOnboardingJob"], Literal["StartInstanceOnboardingJob"], Literal["UpdateCampaignOutboundCallConfig"], Literal["PutDialRequestBatch"], Literal["ListCampaigns"], Literal["DeleteConnectInstanceConfig"], Literal["ResumeCampaign"], Literal["StopCampaign"], Literal["PauseCampaign"], Literal["GetConnectInstanceConfig"], Literal["ListTagsForResource"], Literal["GetCampaignStateBatch"], Literal["GetInstanceOnboardingJobStatus"], Literal["DeleteCampaign"], Literal["UpdateCampaignDialerConfig"], Literal["TagResource"], Literal["GetCampaignState"], Literal["UpdateCampaignName"], Literal["DescribeCampaign"]]
aws_connect_campaigns_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_connect_campaignsStatement(GenericResourceType[aws_connect_campaigns_privilege_type, aws_connect_campaigns_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    