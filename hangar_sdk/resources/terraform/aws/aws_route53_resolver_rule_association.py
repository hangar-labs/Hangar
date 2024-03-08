from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53ResolverRuleAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    resolver_rule_id: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_rule_association")
    name: Optional[str] = None
    timeouts: Optional[Timeouts] = None
