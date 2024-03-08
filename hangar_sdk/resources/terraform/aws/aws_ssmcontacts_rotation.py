from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DailySettings(AbstractTerraformBlock):
    hour_of_day: int
    minute_of_hour: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="daily_settings")


@define(kw_only=True, slots=False)
class HandOffTime(AbstractTerraformBlock):
    hour_of_day: int
    minute_of_hour: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="hand_off_time")


@define(kw_only=True, slots=False)
class MonthlySettings(AbstractTerraformBlock):
    day_of_month: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="monthly_settings")
    hand_off_time: Optional[Sequence[HandOffTime]] = None


@define(kw_only=True, slots=False)
class End(AbstractTerraformBlock):
    hour_of_day: int
    minute_of_hour: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="end")


@define(kw_only=True, slots=False)
class Start(AbstractTerraformBlock):
    hour_of_day: int
    minute_of_hour: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="start")


@define(kw_only=True, slots=False)
class CoverageTimes(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="coverage_times")
    end: Optional[Sequence[End]] = None
    start: Optional[Sequence[Start]] = None


@define(kw_only=True, slots=False)
class ShiftCoverages(AbstractTerraformBlock):
    map_block_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="shift_coverages")
    coverage_times: Optional[Sequence[CoverageTimes]] = None


@define(kw_only=True, slots=False)
class HandOffTime(AbstractTerraformBlock):
    hour_of_day: int
    minute_of_hour: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="hand_off_time")


@define(kw_only=True, slots=False)
class WeeklySettings(AbstractTerraformBlock):
    day_of_week: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="weekly_settings")
    hand_off_time: Optional[Sequence[HandOffTime]] = None


@define(kw_only=True, slots=False)
class Recurrence(AbstractTerraformBlock):
    number_of_on_calls: int
    recurrence_multiplier: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="recurrence")
    daily_settings: Optional[Sequence[DailySettings]] = None
    monthly_settings: Optional[Sequence[MonthlySettings]] = None
    shift_coverages: Optional[Sequence[ShiftCoverages]] = None
    weekly_settings: Optional[Sequence[WeeklySettings]] = None


@define(kw_only=True, slots=False)
class AwsSsmcontactsRotation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    contact_ids: Sequence[str]
    name: str
    time_zone_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssmcontacts_rotation")
    recurrence: Optional[Sequence[Recurrence]] = None
    start_time: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
