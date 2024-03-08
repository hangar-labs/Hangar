from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ConnectionPoolConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="connection_pool_config")
    connection_borrow_timeout: Optional[int] = None
    init_query: Optional[str] = None
    max_connections_percent: Optional[int] = None
    max_idle_connections_percent: Optional[int] = None
    session_pinning_filters: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbProxyDefaultTargetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_proxy_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_proxy_default_target_group")
    connection_pool_config: Optional[Sequence[ConnectionPoolConfig]] = None
    timeouts: Optional[Timeouts] = None
