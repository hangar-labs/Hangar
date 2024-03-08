from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_acm_pca_privilege_type = Union[Literal["DeletePolicy"], Literal["DeleteCertificateAuthority"], Literal["ListPermissions"], Literal["RestoreCertificateAuthority"], Literal["TagCertificateAuthority"], Literal["PutPolicy"], Literal["DeletePermission"], Literal["ListTags"], Literal["ImportCertificateAuthorityCertificate"], Literal["CreateCertificateAuthorityAuditReport"], Literal["UpdateCertificateAuthority"], Literal["DescribeCertificateAuthority"], Literal["RevokeCertificate"], Literal["GetPolicy"], Literal["IssueCertificate"], Literal["DescribeCertificateAuthorityAuditReport"], Literal["GetCertificateAuthorityCsr"], Literal["GetCertificateAuthorityCertificate"], Literal["GetCertificate"], Literal["CreatePermission"], Literal["ListCertificateAuthorities"], Literal["CreateCertificateAuthority"], Literal["UntagCertificateAuthority"]]
aws_acm_pca_condition_type = Union[Literal["aws:TagKeys"], Literal["acm-pca:TemplateArn"], Literal["aws:RequestTag/${TagKey}"]]

class aws_acm_pcaStatement(GenericResourceType[aws_acm_pca_privilege_type, aws_acm_pca_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    