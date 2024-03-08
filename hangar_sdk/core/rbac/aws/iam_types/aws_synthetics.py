from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_synthetics_privilege_type = Union[Literal["UntagResource"], Literal["UpdateCanary"], Literal["DescribeRuntimeVersions"], Literal["ListGroupResources"], Literal["DescribeCanaries"], Literal["GetGroup"], Literal["AssociateResource"], Literal["CreateGroup"], Literal["DeleteCanary"], Literal["ListTagsForResource"], Literal["StartCanary"], Literal["ListGroups"], Literal["CreateCanary"], Literal["ListAssociatedGroups"], Literal["DescribeCanariesLastRun"], Literal["DeleteGroup"], Literal["DisassociateResource"], Literal["GetCanary"], Literal["GetCanaryRuns"], Literal["TagResource"], Literal["StopCanary"]]
aws_synthetics_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["synthetics:Names"], Literal["aws:RequestTag/${TagKey}"]]

class aws_syntheticsStatement(GenericResourceType[aws_synthetics_privilege_type, aws_synthetics_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    