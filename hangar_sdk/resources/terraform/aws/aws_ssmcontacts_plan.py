from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ChannelTargetInfo(AbstractTerraformBlock):
    contact_channel_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="channel_target_info")
    retry_interval_in_minutes: Optional[int] = None


@define(kw_only=True, slots=False)
class ContactTargetInfo(AbstractTerraformBlock):
    is_essential: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="contact_target_info")
    contact_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Target(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target")
    channel_target_info: Optional[Sequence[ChannelTargetInfo]] = None
    contact_target_info: Optional[Sequence[ContactTargetInfo]] = None


@define(kw_only=True, slots=False)
class Stage(AbstractTerraformBlock):
    duration_in_minutes: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="stage")
    target: Optional[Sequence[Target]] = None


@define(kw_only=True, slots=False)
class AwsSsmcontactsPlan(AbstractTerraformResource):
    _group: Any
    _top_name: str
    contact_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssmcontacts_plan")
    stage: Optional[Sequence[Stage]] = None
