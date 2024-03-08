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
    target_group_identifier: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_groups")
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class Forward(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forward")
    target_groups: Optional[Sequence[TargetGroups]] = None


@define(kw_only=True, slots=False)
class Action(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="action")
    fixed_response: Optional[Sequence[FixedResponse]] = None
    forward: Optional[Sequence[Forward]] = None


@define(kw_only=True, slots=False)
class Match(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="match")
    contains: Optional[str] = None
    exact: Optional[str] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class HeaderMatches(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="header_matches")
    case_sensitive: Optional[bool] = None
    match: Optional[Sequence[Match]] = None


@define(kw_only=True, slots=False)
class Match(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="match")
    exact: Optional[str] = None
    prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class PathMatch(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="path_match")
    case_sensitive: Optional[bool] = None
    match: Optional[Sequence[Match]] = None


@define(kw_only=True, slots=False)
class HttpMatch(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="http_match")
    header_matches: Optional[Sequence[HeaderMatches]] = None
    method: Optional[str] = None
    path_match: Optional[Sequence[PathMatch]] = None


@define(kw_only=True, slots=False)
class Match(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="match")
    http_match: Optional[Sequence[HttpMatch]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpclatticeListenerRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    listener_identifier: str
    name: str
    priority: int
    service_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpclattice_listener_rule")
    action: Optional[Sequence[Action]] = None
    match: Optional[Sequence[Match]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
