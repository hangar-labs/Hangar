from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class MediaInsightsConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="media_insights_configuration")
    configuration_arn: Optional[str] = None
    disabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class AwsChimeVoiceConnectorStreaming(AbstractTerraformResource):
    _group: Any
    _top_name: str
    data_retention: int
    voice_connector_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_chime_voice_connector_streaming")
    disabled: Optional[bool] = None
    media_insights_configuration: Optional[Sequence[MediaInsightsConfiguration]] = None
    streaming_notification_targets: Optional[Sequence[str]] = None
