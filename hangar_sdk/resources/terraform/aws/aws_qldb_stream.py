from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class KinesisConfiguration(AbstractTerraformBlock):
    stream_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="kinesis_configuration")
    aggregation_enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsQldbStream(AbstractTerraformResource):
    _group: Any
    _top_name: str
    inclusive_start_time: str
    ledger_name: str
    role_arn: str
    stream_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_qldb_stream")
    exclusive_end_time: Optional[str] = None
    kinesis_configuration: Optional[Sequence[KinesisConfiguration]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
