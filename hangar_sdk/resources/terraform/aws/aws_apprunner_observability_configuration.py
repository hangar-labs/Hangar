from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class TraceConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="trace_configuration")
    vendor: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsApprunnerObservabilityConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    observability_configuration_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_apprunner_observability_configuration"
    )
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    trace_configuration: Optional[Sequence[TraceConfiguration]] = None
