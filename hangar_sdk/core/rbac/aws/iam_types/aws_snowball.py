from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_snowball_privilege_type = Union[Literal["UpdateJobShipmentState"], Literal["GetJobUnlockCode"], Literal["UpdateJob"], Literal["ListLongTermPricing"], Literal["ListClusterJobs"], Literal["CreateReturnShippingLabel"], Literal["UpdateLongTermPricing"], Literal["CreateLongTermPricing"], Literal["GetSoftwareUpdates"], Literal["ListServiceVersions"], Literal["GetSnowballUsage"], Literal["CreateJob"], Literal["DescribeCluster"], Literal["DescribeAddresses"], Literal["GetJobManifest"], Literal["ListPickupLocations"], Literal["DescribeReturnShippingLabel"], Literal["ListCompatibleImages"], Literal["CreateCluster"], Literal["CancelJob"], Literal["CreateAddress"], Literal["ListJobs"], Literal["UpdateCluster"], Literal["CancelCluster"], Literal["ListClusters"], Literal["DescribeJob"], Literal["DescribeAddress"]]
aws_snowball_condition_type = None

class aws_snowballStatement(GenericResourceType[aws_snowball_privilege_type, aws_snowball_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    