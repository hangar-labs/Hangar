from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_emr_containers_privilege_type = Union[Literal["DeleteJobTemplate"], Literal["DescribeVirtualCluster"], Literal["UntagResource"], Literal["DescribeManagedEndpoint"], Literal["DeleteVirtualCluster"], Literal["ListVirtualClusters"], Literal["StartJobRun"], Literal["CancelJobRun"], Literal["ListTagsForResource"], Literal["ListJobTemplates"], Literal["CreateVirtualCluster"], Literal["DeleteManagedEndpoint"], Literal["CreateManagedEndpoint"], Literal["DescribeJobRun"], Literal["ListJobRuns"], Literal["DescribeJobTemplate"], Literal["CreateJobTemplate"], Literal["TagResource"], Literal["ListManagedEndpoints"], Literal["GetManagedEndpointSessionCredentials"]]
aws_emr_containers_condition_type = Union[Literal["aws:TagKeys"], Literal["emr-containers:ExecutionRoleArn"], Literal["emr-containers:JobTemplateArn"], Literal["aws:RequestTag/${TagKey}"]]

class aws_emr_containersStatement(GenericResourceType[aws_emr_containers_privilege_type, aws_emr_containers_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    