from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRoute53ResolverRules(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_route53_resolver_rules")
    name_regex: Optional[str] = None
    owner_id: Optional[str] = None
    resolver_endpoint_id: Optional[str] = None
    rule_type: Optional[str] = None
    share_status: Optional[str] = None
