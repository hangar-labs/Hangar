from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_acm_privilege_type = Union[Literal["DeleteCertificate"], Literal["ListCertificates"], Literal["ListTagsForCertificate"], Literal["PutAccountConfiguration"], Literal["RemoveTagsFromCertificate"], Literal["GetCertificate"], Literal["GetAccountConfiguration"], Literal["RequestCertificate"], Literal["ResendValidationEmail"], Literal["AddTagsToCertificate"], Literal["ImportCertificate"], Literal["RenewCertificate"], Literal["UpdateCertificateOptions"], Literal["ExportCertificate"], Literal["DescribeCertificate"]]
aws_acm_condition_type = Union[Literal["aws:TagKeys"], Literal["acm:KeyAlgorithm"], Literal["acm:CertificateTransparencyLogging"], Literal["acm:ValidationMethod"], Literal["acm:DomainNames"], Literal["acm:CertificateAuthority"], Literal["aws:RequestTag/${TagKey}"]]

class aws_acmStatement(GenericResourceType[aws_acm_privilege_type, aws_acm_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    