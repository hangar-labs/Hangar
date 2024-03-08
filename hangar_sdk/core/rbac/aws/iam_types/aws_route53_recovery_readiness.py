from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_route53_recovery_readiness_privilege_type = Union[Literal["DeleteResourceSet"], Literal["ListCrossAccountAuthorizations"], Literal["UntagResource"], Literal["DeleteReadinessCheck"], Literal["UpdateResourceSet"], Literal["ListTagsForResources"], Literal["DeleteCell"], Literal["CreateRecoveryGroup"], Literal["GetResourceSet"], Literal["GetCellReadinessSummary"], Literal["CreateReadinessCheck"], Literal["GetReadinessCheckResourceStatus"], Literal["ListCells"], Literal["DeleteCrossAccountAuthorization"], Literal["DeleteRecoveryGroup"], Literal["GetCell"], Literal["GetArchitectureRecommendations"], Literal["CreateResourceSet"], Literal["UpdateCell"], Literal["GetReadinessCheckStatus"], Literal["GetRecoveryGroup"], Literal["GetReadinessCheck"], Literal["GetRecoveryGroupReadinessSummary"], Literal["CreateCrossAccountAuthorization"], Literal["CreateCell"], Literal["ListReadinessChecks"], Literal["ListRecoveryGroups"], Literal["TagResource"], Literal["ListResourceSets"], Literal["ListRules"], Literal["UpdateReadinessCheck"], Literal["UpdateRecoveryGroup"]]
aws_route53_recovery_readiness_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_route53_recovery_readinessStatement(GenericResourceType[aws_route53_recovery_readiness_privilege_type, aws_route53_recovery_readiness_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    