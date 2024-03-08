from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_refactor_spaces_privilege_type = Union[Literal["ListEnvironmentVpcs"], Literal["UntagResource"], Literal["ListEnvironments"], Literal["CreateRoute"], Literal["CreateEnvironment"], Literal["DeleteEnvironment"], Literal["ListRoutes"], Literal["DeleteService"], Literal["CreateService"], Literal["CreateApplication"], Literal["GetEnvironment"], Literal["DeleteRoute"], Literal["ListTagsForResource"], Literal["GetService"], Literal["UpdateRoute"], Literal["PutResourcePolicy"], Literal["DeleteApplication"], Literal["ListApplications"], Literal["GetApplication"], Literal["ListServices"], Literal["GetRoute"], Literal["DeleteResourcePolicy"], Literal["TagResource"], Literal["GetResourcePolicy"]]
aws_refactor_spaces_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["refactor-spaces:SourcePath"], Literal["refactor-spaces:ServiceCreatedByAccount"], Literal["refactor-spaces:ApplicationCreatedByAccount"], Literal["refactor-spaces:CreatedByAccountIds"], Literal["refactor-spaces:RouteCreatedByAccount"], Literal["aws:RequestTag/${TagKey}"]]

class aws_refactor_spacesStatement(GenericResourceType[aws_refactor_spaces_privilege_type, aws_refactor_spaces_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    