from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53ResolverFirewallRuleGroupAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    firewall_rule_group_id: str
    name: str
    priority: int
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53_resolver_firewall_rule_group_association"
    )
    mutation_protection: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
