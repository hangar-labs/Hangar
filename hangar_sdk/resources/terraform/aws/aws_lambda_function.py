from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DeadLetterConfig(AbstractTerraformBlock):
    target_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dead_letter_config")


@define(kw_only=True, slots=False)
class Environment(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="environment")
    variables: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class EphemeralStorage(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ephemeral_storage")
    size: Optional[int] = None


@define(kw_only=True, slots=False)
class FileSystemConfig(AbstractTerraformBlock):
    arn: str
    local_mount_path: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="file_system_config")


@define(kw_only=True, slots=False)
class ImageConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="image_config")
    command: Optional[Sequence[str]] = None
    entry_point: Optional[Sequence[str]] = None
    working_directory: Optional[str] = None


@define(kw_only=True, slots=False)
class LoggingConfig(AbstractTerraformBlock):
    log_format: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="logging_config")
    application_log_level: Optional[str] = None
    log_group: Optional[str] = None
    system_log_level: Optional[str] = None


@define(kw_only=True, slots=False)
class SnapStart(AbstractTerraformBlock):
    apply_on: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="snap_start")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class TracingConfig(AbstractTerraformBlock):
    mode: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tracing_config")


@define(kw_only=True, slots=False)
class VpcConfig(AbstractTerraformBlock):
    security_group_ids: Sequence[str]
    subnet_ids: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vpc_config")
    ipv6_allowed_for_dual_stack: Optional[bool] = None


@define(kw_only=True, slots=False)
class AwsLambdaFunction(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    role: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_function")
    architectures: Optional[Sequence[str]] = None
    code_signing_config_arn: Optional[str] = None
    dead_letter_config: Optional[Sequence[DeadLetterConfig]] = None
    description: Optional[str] = None
    environment: Optional[Sequence[Environment]] = None
    ephemeral_storage: Optional[Sequence[EphemeralStorage]] = None
    file_system_config: Optional[Sequence[FileSystemConfig]] = None
    filename: Optional[str] = None
    handler: Optional[str] = None
    image_config: Optional[Sequence[ImageConfig]] = None
    image_uri: Optional[str] = None
    kms_key_arn: Optional[str] = None
    layers: Optional[Sequence[str]] = None
    logging_config: Optional[Sequence[LoggingConfig]] = None
    memory_size: Optional[int] = None
    package_type: Optional[str] = None
    publish: Optional[bool] = None
    replace_security_groups_on_destroy: Optional[bool] = None
    replacement_security_group_ids: Optional[Sequence[str]] = None
    reserved_concurrent_executions: Optional[int] = None
    runtime: Optional[str] = None
    s3_bucket: Optional[str] = None
    s3_key: Optional[str] = None
    s3_object_version: Optional[str] = None
    skip_destroy: Optional[bool] = None
    snap_start: Optional[Sequence[SnapStart]] = None
    source_code_hash: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeout: Optional[int] = None
    timeouts: Optional[Timeouts] = None
    tracing_config: Optional[Sequence[TracingConfig]] = None
    vpc_config: Optional[Sequence[VpcConfig]] = None
