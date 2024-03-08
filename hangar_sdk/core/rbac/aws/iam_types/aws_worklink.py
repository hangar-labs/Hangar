from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_worklink_privilege_type = Union[Literal["DescribeDomain"], Literal["ListDomains"], Literal["ListWebsiteAuthorizationProviders"], Literal["ListWebsiteCertificateAuthorities"], Literal["UntagResource"], Literal["UpdateFleetMetadata"], Literal["UpdateDomainMetadata"], Literal["DescribeAuditStreamConfiguration"], Literal["DescribeIdentityProviderConfiguration"], Literal["RestoreDomainAccess"], Literal["UpdateCompanyNetworkConfiguration"], Literal["DisassociateWebsiteAuthorizationProvider"], Literal["ListDevices"], Literal["DeleteFleet"], Literal["UpdateIdentityProviderConfiguration"], Literal["DescribeCompanyNetworkConfiguration"], Literal["ListTagsForResource"], Literal["SignOutUser"], Literal["AssociateWebsiteCertificateAuthority"], Literal["RevokeDomainAccess"], Literal["UpdateAuditStreamConfiguration"], Literal["SearchEntity"], Literal["DescribeDevicePolicyConfiguration"], Literal["ListFleets"], Literal["DescribeWebsiteCertificateAuthority"], Literal["UpdateDevicePolicyConfiguration"], Literal["DescribeFleetMetadata"], Literal["DisassociateWebsiteCertificateAuthority"], Literal["AssociateDomain"], Literal["TagResource"], Literal["DisassociateDomain"], Literal["DescribeDevice"], Literal["AssociateWebsiteAuthorizationProvider"], Literal["CreateFleet"]]
aws_worklink_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_worklinkStatement(GenericResourceType[aws_worklink_privilege_type, aws_worklink_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    