from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_servicequotas_privilege_type = Union[Literal["GetServiceQuota"], Literal["ListAWSDefaultServiceQuotas"], Literal["UntagResource"], Literal["GetServiceQuotaIncreaseRequestFromTemplate"], Literal["ListServiceQuotas"], Literal["PutServiceQuotaIncreaseRequestIntoTemplate"], Literal["DeleteServiceQuotaIncreaseRequestFromTemplate"], Literal["RequestServiceQuotaIncrease"], Literal["GetRequestedServiceQuotaChange"], Literal["ListTagsForResource"], Literal["GetAWSDefaultServiceQuota"], Literal["DisassociateServiceQuotaTemplate"], Literal["ListRequestedServiceQuotaChangeHistory"], Literal["ListServiceQuotaIncreaseRequestsInTemplate"], Literal["GetAssociationForServiceQuotaTemplate"], Literal["ListServices"], Literal["ListRequestedServiceQuotaChangeHistoryByQuota"], Literal["TagResource"], Literal["AssociateServiceQuotaTemplate"]]
aws_servicequotas_condition_type = Union[Literal["aws:TagKeys"], Literal["servicequotas:service"], Literal["aws:RequestTag/${TagKey}"]]

class aws_servicequotasStatement(GenericResourceType[aws_servicequotas_privilege_type, aws_servicequotas_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    