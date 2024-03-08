from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_backup_gateway_privilege_type = Union[Literal["UpdateHypervisor"], Literal["GetBandwidthRateLimitSchedule"], Literal["UpdateGatewaySoftwareNow"], Literal["UntagResource"], Literal["GetHypervisorPropertyMappings"], Literal["PutHypervisorPropertyMappings"], Literal["ListVirtualMachines"], Literal["GetGateway"], Literal["PutMaintenanceStartTime"], Literal["Restore"], Literal["ListTagsForResource"], Literal["GetHypervisor"], Literal["CreateGateway"], Literal["AssociateGatewayToServer"], Literal["TestHypervisorConfiguration"], Literal["ImportHypervisorConfiguration"], Literal["StartVirtualMachinesMetadataSync"], Literal["DisassociateGatewayFromServer"], Literal["ListHypervisors"], Literal["ListGateways"], Literal["PutBandwidthRateLimitSchedule"], Literal["DeleteGateway"], Literal["UpdateGatewayInformation"], Literal["TagResource"], Literal["GetVirtualMachine"], Literal["Backup"], Literal["DeleteHypervisor"]]
aws_backup_gateway_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_backup_gatewayStatement(GenericResourceType[aws_backup_gateway_privilege_type, aws_backup_gateway_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    