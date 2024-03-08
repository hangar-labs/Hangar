from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class LoggingConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="logging_configuration")
    include_execution_data: Optional[bool] = None
    level: Optional[str] = None
    log_destination: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class TracingConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tracing_configuration")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AwsSfnStateMachine(AbstractTerraformResource):
    _group: Any
    _top_name: str
    definition: str
    role_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sfn_state_machine")
    logging_configuration: Optional[Sequence[LoggingConfiguration]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    publish: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    tracing_configuration: Optional[Sequence[TracingConfiguration]] = None
    type: Optional[str] = None
