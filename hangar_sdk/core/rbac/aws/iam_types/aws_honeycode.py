from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_honeycode_privilege_type = Union[Literal["DeregisterGroups"], Literal["StartTableDataImportJob"], Literal["GetScreenData"], Literal["ListDomains"], Literal["UntagResource"], Literal["ApproveTeamAssociation"], Literal["BatchUpdateTableRows"], Literal["ListTables"], Literal["RestartDomainVerification"], Literal["BatchDeleteTableRows"], Literal["QueryTableRows"], Literal["ListTagsForResource"], Literal["CreateTenant"], Literal["UpdateTeam"], Literal["InvokeScreenAutomation"], Literal["RejectTeamAssociation"], Literal["BatchCreateTableRows"], Literal["ListGroups"], Literal["ListTenants"], Literal["ListTeamAssociations"], Literal["CreateTeam"], Literal["BatchUpsertTableRows"], Literal["DeleteDomains"], Literal["ListTableRows"], Literal["TagResource"], Literal["DescribeTeam"], Literal["RegisterDomainForVerification"], Literal["DescribeTableDataImportJob"], Literal["RegisterGroups"], Literal["ListTableColumns"]]
aws_honeycode_condition_type = None

class aws_honeycodeStatement(GenericResourceType[aws_honeycode_privilege_type, aws_honeycode_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    