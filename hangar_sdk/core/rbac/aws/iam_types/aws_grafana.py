from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_grafana_privilege_type = Union[Literal["ListWorkspaces"], Literal["DisassociateLicense"], Literal["ListPermissions"], Literal["UntagResource"], Literal["UpdateWorkspaceConfiguration"], Literal["ListVersions"], Literal["DescribeWorkspaceConfiguration"], Literal["CreateWorkspace"], Literal["AssociateLicense"], Literal["DescribeWorkspace"], Literal["ListTagsForResource"], Literal["DeleteWorkspaceApiKey"], Literal["DescribeWorkspaceAuthentication"], Literal["CreateWorkspaceApiKey"], Literal["UpdateWorkspaceAuthentication"], Literal["DeleteWorkspace"], Literal["TagResource"], Literal["UpdatePermissions"], Literal["UpdateWorkspace"]]
aws_grafana_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_grafanaStatement(GenericResourceType[aws_grafana_privilege_type, aws_grafana_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    