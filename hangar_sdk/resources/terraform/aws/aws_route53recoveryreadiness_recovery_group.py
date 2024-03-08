from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53recoveryreadinessRecoveryGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    recovery_group_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53recoveryreadiness_recovery_group"
    )
    cells: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
