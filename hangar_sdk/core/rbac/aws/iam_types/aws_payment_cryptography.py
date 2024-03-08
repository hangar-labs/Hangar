from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_payment_cryptography_privilege_type = Union[Literal["GenerateCardValidationData"], Literal["ExportKey"], Literal["UntagResource"], Literal["VerifyMac"], Literal["DecryptData"], Literal["ListKeys"], Literal["GenerateMac"], Literal["DeleteAlias"], Literal["VerifyCardValidationData"], Literal["ListTagsForResource"], Literal["TranslatePinData"], Literal["EncryptData"], Literal["GetParametersForExport"], Literal["UpdateAlias"], Literal["GeneratePinData"], Literal["CreateAlias"], Literal["StopKeyUsage"], Literal["VerifyPinData"], Literal["GetKey"], Literal["ReEncryptData"], Literal["StartKeyUsage"], Literal["TagResource"], Literal["GetAlias"], Literal["CreateKey"], Literal["ListAliases"], Literal["DeleteKey"], Literal["RestoreKey"], Literal["GetPublicKeyCertificate"], Literal["VerifyAuthRequestCryptogram"], Literal["ImportKey"], Literal["GetParametersForImport"]]
aws_payment_cryptography_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_payment_cryptographyStatement(GenericResourceType[aws_payment_cryptography_privilege_type, aws_payment_cryptography_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    