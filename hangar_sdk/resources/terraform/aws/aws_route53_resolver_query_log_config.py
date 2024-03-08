from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53ResolverQueryLogConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination_arn: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_resolver_query_log_config")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
