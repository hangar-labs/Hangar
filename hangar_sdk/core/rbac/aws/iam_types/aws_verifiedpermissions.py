from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_verifiedpermissions_privilege_type = Union[Literal["DeletePolicy"], Literal["ListIdentitySources"], Literal["DeletePolicyStore"], Literal["ListPolicies"], Literal["UpdatePolicyStore"], Literal["GetIdentitySource"], Literal["DeleteIdentitySource"], Literal["UpdatePolicyTemplate"], Literal["ListPolicyTemplates"], Literal["GetSchema"], Literal["GetPolicyTemplate"], Literal["UpdateIdentitySource"], Literal["UpdatePolicy"], Literal["DeletePolicyTemplate"], Literal["ListPolicyStores"], Literal["GetPolicyStore"], Literal["CreatePolicy"], Literal["GetPolicy"], Literal["IsAuthorized"], Literal["CreateIdentitySource"], Literal["CreatePolicyTemplate"], Literal["PutSchema"], Literal["CreatePolicyStore"], Literal["IsAuthorizedWithToken"]]
aws_verifiedpermissions_condition_type = None

class aws_verifiedpermissionsStatement(GenericResourceType[aws_verifiedpermissions_privilege_type, aws_verifiedpermissions_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    