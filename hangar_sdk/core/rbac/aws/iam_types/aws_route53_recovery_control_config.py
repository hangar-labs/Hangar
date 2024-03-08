from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_route53_recovery_control_config_privilege_type = Union[Literal["UpdateControlPanel"], Literal["DeleteCluster"], Literal["DescribeRoutingControlByName"], Literal["UntagResource"], Literal["CreateControlPanel"], Literal["ListRoutingControls"], Literal["UpdateSafetyRule"], Literal["ListSafetyRules"], Literal["ListAssociatedRoute53HealthChecks"], Literal["DeleteRoutingControl"], Literal["DeleteSafetyRule"], Literal["ListTagsForResource"], Literal["DescribeControlPanel"], Literal["ListControlPanels"], Literal["DescribeCluster"], Literal["CreateSafetyRule"], Literal["DescribeRoutingControl"], Literal["CreateCluster"], Literal["UpdateRoutingControl"], Literal["DescribeSafetyRule"], Literal["TagResource"], Literal["DeleteControlPanel"], Literal["ListClusters"], Literal["CreateRoutingControl"], Literal["GetResourcePolicy"]]
aws_route53_recovery_control_config_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_route53_recovery_control_configStatement(GenericResourceType[aws_route53_recovery_control_config_privilege_type, aws_route53_recovery_control_config_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    