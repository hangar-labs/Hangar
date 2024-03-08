from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PlayerLatencyPolicy(AbstractTerraformBlock):
    maximum_individual_player_latency_milliseconds: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="player_latency_policy")
    policy_duration_seconds: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsGameliftGameSessionQueue(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_gamelift_game_session_queue")
    custom_event_data: Optional[str] = None
    destinations: Optional[Sequence[str]] = None
    notification_target: Optional[str] = None
    player_latency_policy: Optional[Sequence[PlayerLatencyPolicy]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeout_in_seconds: Optional[int] = None
