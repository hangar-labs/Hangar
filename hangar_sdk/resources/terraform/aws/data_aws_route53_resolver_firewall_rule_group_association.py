from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRoute53ResolverFirewallRuleGroupAssociation(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    firewall_rule_group_association_id: str
    _block_type: str = "datasource"
    _name: str = field(
        alias="_name", default="aws_route53_resolver_firewall_rule_group_association"
    )
