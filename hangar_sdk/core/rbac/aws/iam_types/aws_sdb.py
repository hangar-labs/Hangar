from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sdb_privilege_type = Union[Literal["DeleteAttributes"], Literal["PutAttributes"], Literal["ListDomains"], Literal["Select"], Literal["BatchPutAttributes"], Literal["BatchDeleteAttributes"], Literal["DeleteDomain"], Literal["CreateDomain"], Literal["DomainMetadata"], Literal["GetAttributes"]]
aws_sdb_condition_type = None

class aws_sdbStatement(GenericResourceType[aws_sdb_privilege_type, aws_sdb_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    