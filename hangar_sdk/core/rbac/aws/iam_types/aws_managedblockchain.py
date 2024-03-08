from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_managedblockchain_privilege_type = Union[Literal["UntagResource"], Literal["ListMembers"], Literal["ListProposals"], Literal["GetNetwork"], Literal["CreateNode"], Literal["GetAccessor"], Literal["POST"], Literal["ListNetworks"], Literal["GET"], Literal["ListNodes"], Literal["ListProposalVotes"], Literal["UpdateNode"], Literal["UpdateMember"], Literal["DeleteAccessor"], Literal["ListTagsForResource"], Literal["InvokeRpcPolygonMainnet"], Literal["VoteOnProposal"], Literal["CreateAccessor"], Literal["InvokeRpcPolygonMumbaiTestnet"], Literal["GetNode"], Literal["GetMember"], Literal["CreateMember"], Literal["ListInvitations"], Literal["InvokeRpcBitcoinMainnet"], Literal["ListAccessors"], Literal["GetProposal"], Literal["Invoke"], Literal["DeleteMember"], Literal["CreateProposal"], Literal["RejectInvitation"], Literal["TagResource"], Literal["InvokeRpcBitcoinTestnet"], Literal["CreateNetwork"], Literal["DeleteNode"]]
aws_managedblockchain_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_managedblockchainStatement(GenericResourceType[aws_managedblockchain_privilege_type, aws_managedblockchain_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    