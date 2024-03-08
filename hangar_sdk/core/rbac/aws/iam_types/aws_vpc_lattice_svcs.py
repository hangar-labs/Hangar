from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_vpc_lattice_svcs_privilege_type = Union[Literal["Invoke"]]
aws_vpc_lattice_svcs_condition_type = Union[Literal["vpc-lattice-svcs:RequestQueryString/${QueryStringKey}"], Literal["vpc-lattice-svcs:RequestHeader/${HeaderName}"], Literal["vpc-lattice-svcs:SourceVpcOwnerAccount"], Literal["vpc-lattice-svcs:ServiceArn"], Literal["vpc-lattice-svcs:ServiceNetworkArn"], Literal["vpc-lattice-svcs:Port"], Literal["vpc-lattice-svcs:SourceVpc"]]

class aws_vpc_lattice_svcsStatement(GenericResourceType[aws_vpc_lattice_svcs_privilege_type, aws_vpc_lattice_svcs_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    