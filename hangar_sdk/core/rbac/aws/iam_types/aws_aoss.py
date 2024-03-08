from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_aoss_privilege_type = Union[Literal["BatchGetCollection"], Literal["CreateSecurityPolicy"], Literal["UntagResource"], Literal["UpdateCollection"], Literal["UpdateVpcEndpoint"], Literal["DeleteVpcEndpoint"], Literal["GetPoliciesStats"], Literal["ListSecurityPolicies"], Literal["GetSecurityConfig"], Literal["ListSecurityConfigs"], Literal["GetSecurityPolicy"], Literal["CreateLifecyclePolicy"], Literal["GetAccountSettings"], Literal["BatchGetLifecyclePolicy"], Literal["ListTagsForResource"], Literal["DeleteSecurityConfig"], Literal["UpdateLifecyclePolicy"], Literal["UpdateAccessPolicy"], Literal["DeleteSecurityPolicy"], Literal["UpdateSecurityConfig"], Literal["DeleteLifecyclePolicy"], Literal["ListLifecyclePolicies"], Literal["ListAccessPolicies"], Literal["BatchGetVpcEndpoint"], Literal["GetAccessPolicy"], Literal["ListCollections"], Literal["ListVpcEndpoints"], Literal["UpdateSecurityPolicy"], Literal["DashboardsAccessAll"], Literal["CreateAccessPolicy"], Literal["BatchGetEffectiveLifecyclePolicy"], Literal["DeleteCollection"], Literal["TagResource"], Literal["CreateVpcEndpoint"], Literal["UpdateAccountSettings"], Literal["DeleteAccessPolicy"], Literal["APIAccessAll"], Literal["CreateSecurityConfig"], Literal["CreateCollection"]]
aws_aoss_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"], Literal["aoss:index"], Literal["aoss:collection"]]

class aws_aossStatement(GenericResourceType[aws_aoss_privilege_type, aws_aoss_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    