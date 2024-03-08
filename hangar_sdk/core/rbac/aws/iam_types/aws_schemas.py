from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_schemas_privilege_type = Union[Literal["UntagResource"], Literal["ListRegistries"], Literal["DescribeRegistry"], Literal["DescribeDiscoverer"], Literal["StopDiscoverer"], Literal["UpdateRegistry"], Literal["StartDiscoverer"], Literal["CreateDiscoverer"], Literal["DeleteSchemaVersion"], Literal["DescribeCodeBinding"], Literal["ExportSchema"], Literal["DescribeSchema"], Literal["ListTagsForResource"], Literal["DeleteDiscoverer"], Literal["PutCodeBinding"], Literal["ListSchemaVersions"], Literal["ListSchemas"], Literal["DeleteSchema"], Literal["PutResourcePolicy"], Literal["ListDiscoverers"], Literal["UpdateDiscoverer"], Literal["GetCodeBindingSource"], Literal["GetDiscoveredSchema"], Literal["UpdateSchema"], Literal["SearchSchemas"], Literal["DeleteResourcePolicy"], Literal["DeleteRegistry"], Literal["TagResource"], Literal["CreateSchema"], Literal["CreateRegistry"], Literal["GetResourcePolicy"]]
aws_schemas_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_schemasStatement(GenericResourceType[aws_schemas_privilege_type, aws_schemas_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    