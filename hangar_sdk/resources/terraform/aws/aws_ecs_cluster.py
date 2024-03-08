from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class LogConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="log_configuration")
    cloud_watch_encryption_enabled: Optional[bool] = None
    cloud_watch_log_group_name: Optional[str] = None
    s3_bucket_encryption_enabled: Optional[bool] = None
    s3_bucket_name: Optional[str] = None
    s3_key_prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class ExecuteCommandConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="execute_command_configuration")
    kms_key_id: Optional[str] = None
    log_configuration: Optional[Sequence[LogConfiguration]] = None
    logging: Optional[str] = None


@define(kw_only=True, slots=False)
class Configuration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="configuration")
    execute_command_configuration: Optional[Sequence[ExecuteCommandConfiguration]] = (
        None
    )


@define(kw_only=True, slots=False)
class ServiceConnectDefaults(AbstractTerraformBlock):
    namespace: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="service_connect_defaults")


@define(kw_only=True, slots=False)
class Setting(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="setting")


@define(kw_only=True, slots=False)
class AwsEcsCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_cluster")
    configuration: Optional[Sequence[Configuration]] = None
    service_connect_defaults: Optional[Sequence[ServiceConnectDefaults]] = None
    setting: Optional[Sequence[Setting]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
