from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53ResolverFirewallConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    resource_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_firewall_config")
    firewall_fail_open: Optional[str] = None
