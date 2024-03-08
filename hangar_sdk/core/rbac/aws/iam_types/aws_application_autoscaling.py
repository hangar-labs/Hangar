from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_application_autoscaling_privilege_type = Union[Literal["DescribeScheduledActions"], Literal["DeleteScheduledAction"], Literal["PutScalingPolicy"], Literal["DeregisterScalableTarget"], Literal["RegisterScalableTarget"], Literal["UntagResource"], Literal["DescribeScalingPolicies"], Literal["DescribeScalingActivities"], Literal["TagResource"], Literal["ListTagsForResource"], Literal["DescribeScalableTargets"], Literal["DeleteScalingPolicy"], Literal["PutScheduledAction"]]
aws_application_autoscaling_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"], Literal["application-autoscaling:service-namespace"], Literal["application-autoscaling:scalable-dimension"]]

class aws_application_autoscalingStatement(GenericResourceType[aws_application_autoscaling_privilege_type, aws_application_autoscaling_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    