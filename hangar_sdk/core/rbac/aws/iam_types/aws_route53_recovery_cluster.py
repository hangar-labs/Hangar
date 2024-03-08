from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_route53_recovery_cluster_privilege_type = Union[Literal["UpdateRoutingControlStates"], Literal["UpdateRoutingControlState"], Literal["ListRoutingControls"], Literal["GetRoutingControlState"]]
aws_route53_recovery_cluster_condition_type = Union[Literal["route53-recovery-cluster:AllowSafetyRulesOverrides"]]

class aws_route53_recovery_clusterStatement(GenericResourceType[aws_route53_recovery_cluster_privilege_type, aws_route53_recovery_cluster_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    