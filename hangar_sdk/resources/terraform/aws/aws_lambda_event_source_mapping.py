from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AmazonManagedKafkaEventSourceConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(
        alias="_name", default="amazon_managed_kafka_event_source_config"
    )
    consumer_group_id: Optional[str] = None


@define(kw_only=True, slots=False)
class OnFailure(AbstractTerraformBlock):
    destination_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="on_failure")


@define(kw_only=True, slots=False)
class DestinationConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination_config")
    on_failure: Optional[Sequence[OnFailure]] = None


@define(kw_only=True, slots=False)
class DocumentDbEventSourceConfig(AbstractTerraformBlock):
    database_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="document_db_event_source_config")
    collection_name: Optional[str] = None
    full_document: Optional[str] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    pattern: Optional[str] = None


@define(kw_only=True, slots=False)
class FilterCriteria(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter_criteria")
    filter: Optional[Sequence[Filter]] = None


@define(kw_only=True, slots=False)
class ScalingConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scaling_config")
    maximum_concurrency: Optional[int] = None


@define(kw_only=True, slots=False)
class SelfManagedEventSource(AbstractTerraformBlock):
    endpoints: Dict[str, str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="self_managed_event_source")


@define(kw_only=True, slots=False)
class SelfManagedKafkaEventSourceConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="self_managed_kafka_event_source_config")
    consumer_group_id: Optional[str] = None


@define(kw_only=True, slots=False)
class SourceAccessConfiguration(AbstractTerraformBlock):
    type: str
    uri: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_access_configuration")


@define(kw_only=True, slots=False)
class AwsLambdaEventSourceMapping(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_event_source_mapping")
    amazon_managed_kafka_event_source_config: Optional[
        Sequence[AmazonManagedKafkaEventSourceConfig]
    ] = None
    batch_size: Optional[int] = None
    bisect_batch_on_function_error: Optional[bool] = None
    destination_config: Optional[Sequence[DestinationConfig]] = None
    document_db_event_source_config: Optional[Sequence[DocumentDbEventSourceConfig]] = (
        None
    )
    enabled: Optional[bool] = None
    event_source_arn: Optional[str] = None
    filter_criteria: Optional[Sequence[FilterCriteria]] = None
    function_response_types: Optional[Sequence[str]] = None
    maximum_batching_window_in_seconds: Optional[int] = None
    maximum_record_age_in_seconds: Optional[int] = None
    maximum_retry_attempts: Optional[int] = None
    parallelization_factor: Optional[int] = None
    queues: Optional[Sequence[str]] = None
    scaling_config: Optional[Sequence[ScalingConfig]] = None
    self_managed_event_source: Optional[Sequence[SelfManagedEventSource]] = None
    self_managed_kafka_event_source_config: Optional[
        Sequence[SelfManagedKafkaEventSourceConfig]
    ] = None
    source_access_configuration: Optional[Sequence[SourceAccessConfiguration]] = None
    starting_position: Optional[str] = None
    starting_position_timestamp: Optional[str] = None
    topics: Optional[Sequence[str]] = None
    tumbling_window_in_seconds: Optional[int] = None
