from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_network_firewall_privilege_type = Union[Literal["UntagResource"], Literal["UpdateTLSInspectionConfiguration"], Literal["DescribeFirewall"], Literal["DescribeFirewallPolicy"], Literal["CreateFirewall"], Literal["UpdateLoggingConfiguration"], Literal["UpdateFirewallPolicy"], Literal["DeleteTLSInspectionConfiguration"], Literal["DescribeRuleGroup"], Literal["UpdateFirewallDeleteProtection"], Literal["CreateRuleGroup"], Literal["DescribeResourcePolicy"], Literal["ListTLSInspectionConfigurations"], Literal["UpdateFirewallEncryptionConfiguration"], Literal["DescribeTLSInspectionConfiguration"], Literal["ListTagsForResource"], Literal["AssociateSubnets"], Literal["DeleteFirewall"], Literal["DisassociateSubnets"], Literal["DeleteRuleGroup"], Literal["CreateFirewallPolicy"], Literal["UpdateSubnetChangeProtection"], Literal["AssociateFirewallPolicy"], Literal["PutResourcePolicy"], Literal["ListFirewalls"], Literal["UpdateRuleGroup"], Literal["UpdateFirewallPolicyChangeProtection"], Literal["ListRuleGroups"], Literal["DeleteResourcePolicy"], Literal["TagResource"], Literal["DescribeLoggingConfiguration"], Literal["CreateTLSInspectionConfiguration"], Literal["ListFirewallPolicies"], Literal["DeleteFirewallPolicy"], Literal["DescribeRuleGroupMetadata"], Literal["UpdateFirewallDescription"]]
aws_network_firewall_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_network_firewallStatement(GenericResourceType[aws_network_firewall_privilege_type, aws_network_firewall_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    