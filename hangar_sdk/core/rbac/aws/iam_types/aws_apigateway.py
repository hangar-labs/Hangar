from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_apigateway_privilege_type = Union[Literal["POST"], Literal["PATCH"], Literal["GET"], Literal["RemoveCertificateFromDomain"], Literal["SetWebACL"], Literal["PUT"], Literal["DELETE"], Literal["AddCertificateToDomain"], Literal["UpdateRestApiPolicy"]]
aws_apigateway_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_apigatewayStatement(GenericResourceType[aws_apigateway_privilege_type, aws_apigateway_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    