from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    read: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsLbListener(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_lb_listener")
    arn: Optional[str] = None
    load_balancer_arn: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
