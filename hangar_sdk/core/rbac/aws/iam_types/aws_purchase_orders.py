from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_purchase_orders_privilege_type = Union[Literal["DeletePurchaseOrder"], Literal["GetConsoleActionSetEnforced"], Literal["GetPurchaseOrder"], Literal["UntagResource"], Literal["ViewPurchaseOrders"], Literal["UpdatePurchaseOrderStatus"], Literal["TagResource"], Literal["ListPurchaseOrders"], Literal["UpdateConsoleActionSetEnforced"], Literal["ListPurchaseOrderInvoices"], Literal["ListTagsForResource"], Literal["UpdatePurchaseOrder"], Literal["AddPurchaseOrder"], Literal["ModifyPurchaseOrders"]]
aws_purchase_orders_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_purchase_ordersStatement(GenericResourceType[aws_purchase_orders_privilege_type, aws_purchase_orders_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    