from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Targets(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="targets")


@define(kw_only=True, slots=False)
class AwsSsmMaintenanceWindowTarget(AbstractTerraformResource):
    _group: Any
    _top_name: str
    resource_type: str
    window_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_maintenance_window_target")
    description: Optional[str] = None
    name: Optional[str] = None
    owner_information: Optional[str] = None
    targets: Optional[Sequence[Targets]] = None
