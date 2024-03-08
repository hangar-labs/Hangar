from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_panorama_privilege_type = Union[Literal["DescribeNodeFromTemplateJob"], Literal["DescribePackageImportJob"], Literal["ListNodeFromTemplateJobs"], Literal["DescribeDeviceJob"], Literal["GetWebSocketURL"], Literal["UntagResource"], Literal["DescribeApplicationInstance"], Literal["CreateJobForDevices"], Literal["ProvisionDevice"], Literal["DeregisterPackageVersion"], Literal["DescribePackageVersion"], Literal["ListNodes"], Literal["DescribeSoftware"], Literal["ListDevices"], Literal["UpdateDeviceMetadata"], Literal["ListTagsForResource"], Literal["DeleteDevice"], Literal["DeletePackage"], Literal["CreateNodeFromTemplateJob"], Literal["ListPackageImportJobs"], Literal["RegisterPackageVersion"], Literal["RemoveApplicationInstance"], Literal["ListApplicationInstances"], Literal["ListPackages"], Literal["CreatePackageImportJob"], Literal["ListApplicationInstanceNodeInstances"], Literal["ListApplicationInstanceDependencies"], Literal["DescribePackage"], Literal["ListDevicesJobs"], Literal["CreateApplicationInstance"], Literal["SignalApplicationInstanceNodeInstances"], Literal["CreatePackage"], Literal["TagResource"], Literal["DescribeNode"], Literal["DescribeDevice"], Literal["DescribeApplicationInstanceDetails"]]
aws_panorama_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_panoramaStatement(GenericResourceType[aws_panorama_privilege_type, aws_panorama_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    