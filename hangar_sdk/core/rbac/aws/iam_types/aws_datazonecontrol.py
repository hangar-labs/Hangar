from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_datazonecontrol_privilege_type = Union[Literal["GetAssociatedDomain"], Literal["ListDomains"], Literal["UntagResource"], Literal["ListAssociatedEnvironments"], Literal["DeleteEnvironment"], Literal["CreateEnvironment"], Literal["ListMetadataCollectorRuns"], Literal["UpdateAccountAssociationDescription"], Literal["UpdateDataSource"], Literal["GetUserPortalLoginAuthCode"], Literal["CreateAccountAssociationInvitation"], Literal["ListMetadataCollectors"], Literal["DissociateAccount"], Literal["ListDataSources"], Literal["GetEnvironment"], Literal["ListAllAssociatedAccountsForEnvironment"], Literal["ListTagsForResource"], Literal["ListProjects"], Literal["ListAccountAssociationInvitations"], Literal["UpdateEnvironment"], Literal["GetDomain"], Literal["GetMetadataCollector"], Literal["CreateDataSource"], Literal["ListEnvironment"], Literal["ListDataSourcesByEnvironment"], Literal["GetDataSourceByEnvironment"], Literal["TagResource"], Literal["ReviewAccountAssociationInvitation"], Literal["DeleteDataSource"]]
aws_datazonecontrol_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_datazonecontrolStatement(GenericResourceType[aws_datazonecontrol_privilege_type, aws_datazonecontrol_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    