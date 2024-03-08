from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class FixedResponse(AbstractTerraformBlock):
    status_code: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="fixed_response")


@define(kw_only=True, slots=False)
class TargetGroups(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_groups")
    target_group_identifier: Optional[str] = None
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class Forward(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forward")
    target_groups: Optional[Sequence[TargetGroups]] = None


@define(kw_only=True, slots=False)
class DefaultAction(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_action")
    fixed_response: Optional[Sequence[FixedResponse]] = None
    forward: Optional[Sequence[Forward]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpclatticeListener(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    protocol: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpclattice_listener")
    default_action: Optional[Sequence[DefaultAction]] = None
    port: Optional[int] = None
    service_arn: Optional[str] = None
    service_identifier: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
