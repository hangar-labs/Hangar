from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CloudwatchDestination(AbstractTerraformBlock):
    default_value: str
    dimension_name: str
    value_source: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloudwatch_destination")


@define(kw_only=True, slots=False)
class KinesisDestination(AbstractTerraformBlock):
    role_arn: str
    stream_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="kinesis_destination")


@define(kw_only=True, slots=False)
class SnsDestination(AbstractTerraformBlock):
    topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sns_destination")


@define(kw_only=True, slots=False)
class AwsSesEventDestination(AbstractTerraformResource):
    _group: Any
    _top_name: str
    configuration_set_name: str
    matching_types: Sequence[str]
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_event_destination")
    cloudwatch_destination: Optional[Sequence[CloudwatchDestination]] = None
    enabled: Optional[bool] = None
    kinesis_destination: Optional[Sequence[KinesisDestination]] = None
    sns_destination: Optional[Sequence[SnsDestination]] = None
