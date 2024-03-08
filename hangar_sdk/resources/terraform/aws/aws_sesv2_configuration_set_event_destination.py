from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DimensionConfiguration(AbstractTerraformBlock):
    default_dimension_value: str
    dimension_name: str
    dimension_value_source: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dimension_configuration")


@define(kw_only=True, slots=False)
class CloudWatchDestination(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloud_watch_destination")
    dimension_configuration: Optional[Sequence[DimensionConfiguration]] = None


@define(kw_only=True, slots=False)
class KinesisFirehoseDestination(AbstractTerraformBlock):
    delivery_stream_arn: str
    iam_role_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="kinesis_firehose_destination")


@define(kw_only=True, slots=False)
class PinpointDestination(AbstractTerraformBlock):
    application_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="pinpoint_destination")


@define(kw_only=True, slots=False)
class SnsDestination(AbstractTerraformBlock):
    topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sns_destination")


@define(kw_only=True, slots=False)
class EventDestination(AbstractTerraformBlock):
    matching_event_types: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="event_destination")
    cloud_watch_destination: Optional[Sequence[CloudWatchDestination]] = None
    enabled: Optional[bool] = None
    kinesis_firehose_destination: Optional[Sequence[KinesisFirehoseDestination]] = None
    pinpoint_destination: Optional[Sequence[PinpointDestination]] = None
    sns_destination: Optional[Sequence[SnsDestination]] = None


@define(kw_only=True, slots=False)
class AwsSesv2ConfigurationSetEventDestination(AbstractTerraformResource):
    _group: Any
    _top_name: str
    configuration_set_name: str
    event_destination_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_sesv2_configuration_set_event_destination"
    )
    event_destination: Optional[Sequence[EventDestination]] = None
