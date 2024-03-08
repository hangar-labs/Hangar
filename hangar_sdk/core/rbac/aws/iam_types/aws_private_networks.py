from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_private_networks_privilege_type = Union[Literal["GetNetworkResource"], Literal["UntagResource"], Literal["GetNetwork"], Literal["UpdateNetworkSite"], Literal["ListNetworks"], Literal["ConfigureAccessPoint"], Literal["ListDeviceIdentifiers"], Literal["ListTagsForResource"], Literal["GetOrder"], Literal["ActivateDeviceIdentifier"], Literal["ListOrders"], Literal["Ping"], Literal["ListNetworkResources"], Literal["AcknowledgeOrderReceipt"], Literal["DeactivateDeviceIdentifier"], Literal["DeleteNetworkSite"], Literal["ListNetworkSites"], Literal["CreateNetworkSite"], Literal["StartNetworkResourceUpdate"], Literal["ActivateNetworkSite"], Literal["GetDeviceIdentifier"], Literal["TagResource"], Literal["DeleteNetwork"], Literal["UpdateNetworkSitePlan"], Literal["CreateNetwork"], Literal["GetNetworkSite"]]
aws_private_networks_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_private_networksStatement(GenericResourceType[aws_private_networks_privilege_type, aws_private_networks_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    