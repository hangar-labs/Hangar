from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cognito_identity_privilege_type = Union[Literal["UntagResource"], Literal["SetPrincipalTagAttributeMap"], Literal["GetCredentialsForIdentity"], Literal["MergeDeveloperIdentities"], Literal["GetPrincipalTagAttributeMap"], Literal["ListIdentityPools"], Literal["CreateIdentityPool"], Literal["UnlinkDeveloperIdentity"], Literal["DescribeIdentityPool"], Literal["DeleteIdentities"], Literal["DeleteIdentityPool"], Literal["GetOpenIdToken"], Literal["ListIdentities"], Literal["GetIdentityPoolRoles"], Literal["UnlinkIdentity"], Literal["GetIdentityPoolAnalytics"], Literal["GetIdentityProviderDailyAnalytics"], Literal["ListTagsForResource"], Literal["LookupDeveloperIdentity"], Literal["GetOpenIdTokenForDeveloperIdentity"], Literal["GetIdentityPoolDailyAnalytics"], Literal["GetId"], Literal["TagResource"], Literal["UpdateIdentityPool"], Literal["SetIdentityPoolRoles"], Literal["DescribeIdentity"]]
aws_cognito_identity_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cognito_identityStatement(GenericResourceType[aws_cognito_identity_privilege_type, aws_cognito_identity_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    