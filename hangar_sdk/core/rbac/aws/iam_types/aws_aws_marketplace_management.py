from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_aws_marketplace_management_privilege_type = Union[Literal["PutBankAccountVerificationDetails"], Literal["PutAdditionalSellerNotificationRecipients"], Literal["viewMarketing"], Literal["GetBankAccountVerificationDetails"], Literal["viewSupport"], Literal["PutSellerVerificationDetails"], Literal["uploadFiles"], Literal["PutSecondaryUserVerificationDetails"], Literal["viewSettings"], Literal["GetAdditionalSellerNotificationRecipients"], Literal["GetSecondaryUserVerificationDetails"], Literal["viewReports"], Literal["GetSellerVerificationDetails"]]
aws_aws_marketplace_management_condition_type = None

class aws_aws_marketplace_managementStatement(GenericResourceType[aws_aws_marketplace_management_privilege_type, aws_aws_marketplace_management_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    