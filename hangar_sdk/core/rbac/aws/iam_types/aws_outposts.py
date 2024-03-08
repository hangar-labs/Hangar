from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_outposts_privilege_type = Union[Literal["UntagResource"], Literal["ListOutposts"], Literal["UpdateOutpost"], Literal["GetSiteAddress"], Literal["UpdateSiteAddress"], Literal["CreateOrder"], Literal["UpdateSite"], Literal["DeleteOutpost"], Literal["GetConnection"], Literal["GetCatalogItem"], Literal["ListSites"], Literal["ListTagsForResource"], Literal["GetOrder"], Literal["CreatePrivateConnectivityConfig"], Literal["GetOutpostInstanceTypes"], Literal["ListOrders"], Literal["GetSite"], Literal["CreateSite"], Literal["GetPrivateConnectivityConfig"], Literal["CancelOrder"], Literal["ListCatalogItems"], Literal["UpdateSiteRackPhysicalProperties"], Literal["GetOutpost"], Literal["CreateOutpost"], Literal["TagResource"], Literal["ListAssets"], Literal["StartConnection"], Literal["DeleteSite"]]
aws_outposts_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_outpostsStatement(GenericResourceType[aws_outposts_privilege_type, aws_outposts_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    