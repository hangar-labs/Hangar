from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class LogStreams(AbstractTerraformBlock):
    file: str
    log_group_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="log_streams")
    batch_count: Optional[int] = None
    batch_size: Optional[int] = None
    buffer_duration: Optional[int] = None
    datetime_format: Optional[str] = None
    encoding: Optional[str] = None
    file_fingerprint_lines: Optional[str] = None
    initial_position: Optional[str] = None
    multiline_start_pattern: Optional[str] = None
    time_zone: Optional[str] = None


@define(kw_only=True, slots=False)
class CloudwatchConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloudwatch_configuration")
    enabled: Optional[bool] = None
    log_streams: Optional[Sequence[LogStreams]] = None


@define(kw_only=True, slots=False)
class EbsVolume(AbstractTerraformBlock):
    mount_point: str
    number_of_disks: int
    size: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs_volume")
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    raid_level: Optional[str] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class Downscaling(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="downscaling")
    alarms: Optional[Sequence[str]] = None
    cpu_threshold: Optional[int] = None
    ignore_metrics_time: Optional[int] = None
    instance_count: Optional[int] = None
    load_threshold: Optional[int] = None
    memory_threshold: Optional[int] = None
    thresholds_wait_time: Optional[int] = None


@define(kw_only=True, slots=False)
class Upscaling(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="upscaling")
    alarms: Optional[Sequence[str]] = None
    cpu_threshold: Optional[int] = None
    ignore_metrics_time: Optional[int] = None
    instance_count: Optional[int] = None
    load_threshold: Optional[int] = None
    memory_threshold: Optional[int] = None
    thresholds_wait_time: Optional[int] = None


@define(kw_only=True, slots=False)
class LoadBasedAutoScaling(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="load_based_auto_scaling")
    downscaling: Optional[Sequence[Downscaling]] = None
    enable: Optional[bool] = None
    upscaling: Optional[Sequence[Upscaling]] = None


@define(kw_only=True, slots=False)
class AwsOpsworksEcsClusterLayer(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ecs_cluster_arn: str
    stack_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_opsworks_ecs_cluster_layer")
    auto_assign_elastic_ips: Optional[bool] = None
    auto_assign_public_ips: Optional[bool] = None
    auto_healing: Optional[bool] = None
    cloudwatch_configuration: Optional[Sequence[CloudwatchConfiguration]] = None
    custom_configure_recipes: Optional[Sequence[str]] = None
    custom_deploy_recipes: Optional[Sequence[str]] = None
    custom_instance_profile_arn: Optional[str] = None
    custom_json: Optional[str] = None
    custom_security_group_ids: Optional[Sequence[str]] = None
    custom_setup_recipes: Optional[Sequence[str]] = None
    custom_shutdown_recipes: Optional[Sequence[str]] = None
    custom_undeploy_recipes: Optional[Sequence[str]] = None
    drain_elb_on_shutdown: Optional[bool] = None
    ebs_volume: Optional[Sequence[EbsVolume]] = None
    elastic_load_balancer: Optional[str] = None
    install_updates_on_boot: Optional[bool] = None
    instance_shutdown_timeout: Optional[int] = None
    load_based_auto_scaling: Optional[Sequence[LoadBasedAutoScaling]] = None
    name: Optional[str] = None
    system_packages: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    use_ebs_optimized_instances: Optional[bool] = None
