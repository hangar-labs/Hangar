from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")


@define(kw_only=True, slots=False)
class DataAwsRoute53ResolverQueryLogConfig(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_route53_resolver_query_log_config")
    filter: Optional[Sequence[Filter]] = None
    name: Optional[str] = None
    resolver_query_log_config_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
