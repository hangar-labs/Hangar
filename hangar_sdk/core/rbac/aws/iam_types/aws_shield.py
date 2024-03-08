from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_shield_privilege_type = Union[Literal["DeleteProtectionGroup"], Literal["UntagResource"], Literal["CreateSubscription"], Literal["ListAttacks"], Literal["DisassociateDRTRole"], Literal["GetSubscriptionState"], Literal["DescribeAttack"], Literal["DescribeEmergencyContactSettings"], Literal["UpdateSubscription"], Literal["UpdateApplicationLayerAutomaticResponse"], Literal["DisableApplicationLayerAutomaticResponse"], Literal["ListTagsForResource"], Literal["DescribeAttackStatistics"], Literal["CreateProtection"], Literal["DeleteSubscription"], Literal["DescribeSubscription"], Literal["AssociateDRTRole"], Literal["EnableApplicationLayerAutomaticResponse"], Literal["CreateProtectionGroup"], Literal["AssociateProactiveEngagementDetails"], Literal["DisassociateDRTLogBucket"], Literal["AssociateDRTLogBucket"], Literal["EnableProactiveEngagement"], Literal["DescribeProtectionGroup"], Literal["ListProtections"], Literal["AssociateHealthCheck"], Literal["DescribeProtection"], Literal["ListResourcesInProtectionGroup"], Literal["TagResource"], Literal["DeleteProtection"], Literal["UpdateProtectionGroup"], Literal["ListProtectionGroups"], Literal["DisassociateHealthCheck"], Literal["DisableProactiveEngagement"], Literal["UpdateEmergencyContactSettings"], Literal["DescribeDRTAccess"]]
aws_shield_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_shieldStatement(GenericResourceType[aws_shield_privilege_type, aws_shield_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    