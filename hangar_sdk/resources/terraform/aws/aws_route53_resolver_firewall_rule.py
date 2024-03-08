from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53ResolverFirewallRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    action: str
    firewall_domain_list_id: str
    firewall_rule_group_id: str
    name: str
    priority: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_firewall_rule")
    block_override_dns_type: Optional[str] = None
    block_override_domain: Optional[str] = None
    block_override_ttl: Optional[int] = None
    block_response: Optional[str] = None
