from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_batch_privilege_type = Union[Literal["CreateJobQueue"], Literal["UntagResource"], Literal["DeregisterJobDefinition"], Literal["CreateComputeEnvironment"], Literal["DescribeJobDefinitions"], Literal["DescribeJobQueues"], Literal["RegisterJobDefinition"], Literal["UpdateSchedulingPolicy"], Literal["DescribeSchedulingPolicies"], Literal["DescribeJobs"], Literal["TerminateJob"], Literal["DescribeComputeEnvironments"], Literal["DeleteJobQueue"], Literal["SubmitJob"], Literal["ListTagsForResource"], Literal["ListSchedulingPolicies"], Literal["UpdateJobQueue"], Literal["DeleteComputeEnvironment"], Literal["CancelJob"], Literal["CreateSchedulingPolicy"], Literal["ListJobs"], Literal["TagResource"], Literal["DeleteSchedulingPolicy"], Literal["UpdateComputeEnvironment"]]
aws_batch_condition_type = Union[Literal["aws:TagKeys"], Literal["batch:User"], Literal["batch:EKSRunAsUser"], Literal["batch:Privileged"], Literal["batch:EKSServiceAccountName"], Literal["batch:LogDriver"], Literal["batch:EKSRunAsGroup"], Literal["batch:EKSImage"], Literal["batch:EKSPrivileged"], Literal["batch:AWSLogsGroup"], Literal["batch:Image"], Literal["batch:AWSLogsRegion"], Literal["batch:AWSLogsCreateGroup"], Literal["batch:AWSLogsStreamPrefix"], Literal["batch:ShareIdentifier"], Literal["aws:RequestTag/${TagKey}"]]

class aws_batchStatement(GenericResourceType[aws_batch_privilege_type, aws_batch_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    