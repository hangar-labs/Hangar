from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_tnb_privilege_type = Union[Literal["CreateSolNetworkInstance"], Literal["UntagResource"], Literal["InstantiateSolNetworkInstance"], Literal["DeleteSolNetworkPackage"], Literal["DeleteSolNetworkInstance"], Literal["DeleteSolFunctionPackage"], Literal["GetSolNetworkPackageDescriptor"], Literal["ListSolNetworkOperations"], Literal["PutSolFunctionPackageContent"], Literal["UpdateSolNetworkInstance"], Literal["UpdateSolNetworkPackage"], Literal["GetSolFunctionPackage"], Literal["ListSolFunctionInstances"], Literal["GetSolNetworkPackage"], Literal["PutSolNetworkPackageContent"], Literal["CreateSolNetworkPackage"], Literal["GetSolFunctionPackageDescriptor"], Literal["GetSolNetworkPackageContent"], Literal["ListTagsForResource"], Literal["GetSolFunctionPackageContent"], Literal["ListSolNetworkInstances"], Literal["ValidateSolNetworkPackageContent"], Literal["UpdateSolFunctionPackage"], Literal["ListSolNetworkPackages"], Literal["ListSolFunctionPackages"], Literal["TerminateSolNetworkInstance"], Literal["GetSolNetworkOperation"], Literal["CreateSolFunctionPackage"], Literal["CancelSolNetworkOperation"], Literal["TagResource"], Literal["GetSolFunctionInstance"], Literal["ValidateSolFunctionPackageContent"], Literal["GetSolNetworkInstance"]]
aws_tnb_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_tnbStatement(GenericResourceType[aws_tnb_privilege_type, aws_tnb_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    