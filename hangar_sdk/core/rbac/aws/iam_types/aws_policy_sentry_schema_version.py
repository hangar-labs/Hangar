from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_policy_sentry_schema_version_privilege_type = None
aws_policy_sentry_schema_version_condition_type = None

class aws_policy_sentry_schema_versionStatement(GenericResourceType[aws_policy_sentry_schema_version_privilege_type, aws_policy_sentry_schema_version_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    