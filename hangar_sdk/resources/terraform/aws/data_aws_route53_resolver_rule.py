from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRoute53ResolverRule(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_route53_resolver_rule")
    domain_name: Optional[str] = None
    name: Optional[str] = None
    resolver_endpoint_id: Optional[str] = None
    resolver_rule_id: Optional[str] = None
    rule_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
