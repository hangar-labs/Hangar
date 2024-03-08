from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RoutingConfiguration(AbstractTerraformBlock):
    state_machine_version_arn: str
    weight: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="routing_configuration")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSfnAlias(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sfn_alias")
    description: Optional[str] = None
    routing_configuration: Optional[Sequence[RoutingConfiguration]] = None
    timeouts: Optional[Timeouts] = None
