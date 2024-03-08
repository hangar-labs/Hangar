from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_appmesh_privilege_type = Union[Literal["UpdateGatewayRoute"], Literal["DeleteGatewayRoute"], Literal["DescribeVirtualGateway"], Literal["UntagResource"], Literal["CreateVirtualService"], Literal["DescribeVirtualNode"], Literal["CreateRoute"], Literal["CreateMesh"], Literal["CreateVirtualGateway"], Literal["ListRoutes"], Literal["ListVirtualGateways"], Literal["DeleteVirtualNode"], Literal["DescribeVirtualRouter"], Literal["CreateGatewayRoute"], Literal["DeleteVirtualRouter"], Literal["DescribeMesh"], Literal["DeleteRoute"], Literal["ListTagsForResource"], Literal["DeleteMesh"], Literal["DescribeVirtualService"], Literal["DescribeRoute"], Literal["UpdateRoute"], Literal["ListGatewayRoutes"], Literal["UpdateVirtualRouter"], Literal["ListVirtualServices"], Literal["ListMeshes"], Literal["DescribeGatewayRoute"], Literal["UpdateVirtualNode"], Literal["DeleteVirtualService"], Literal["ListVirtualRouters"], Literal["DeleteVirtualGateway"], Literal["CreateVirtualNode"], Literal["StreamAggregatedResources"], Literal["UpdateVirtualService"], Literal["ListVirtualNodes"], Literal["UpdateMesh"], Literal["TagResource"], Literal["UpdateVirtualGateway"], Literal["CreateVirtualRouter"]]
aws_appmesh_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_appmeshStatement(GenericResourceType[aws_appmesh_privilege_type, aws_appmesh_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    