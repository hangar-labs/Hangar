from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EphemeralStorage(AbstractTerraformBlock):
    size_in_gib: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ephemeral_storage")


@define(kw_only=True, slots=False)
class InferenceAccelerator(AbstractTerraformBlock):
    device_name: str
    device_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="inference_accelerator")


@define(kw_only=True, slots=False)
class PlacementConstraints(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="placement_constraints")
    expression: Optional[str] = None


@define(kw_only=True, slots=False)
class ProxyConfiguration(AbstractTerraformBlock):
    container_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="proxy_configuration")
    properties: Optional[Dict[str, str]] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class RuntimePlatform(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="runtime_platform")
    cpu_architecture: Optional[str] = None
    operating_system_family: Optional[str] = None


@define(kw_only=True, slots=False)
class DockerVolumeConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="docker_volume_configuration")
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driver_opts: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None
    scope: Optional[str] = None


@define(kw_only=True, slots=False)
class AuthorizationConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authorization_config")
    access_point_id: Optional[str] = None
    iam: Optional[str] = None


@define(kw_only=True, slots=False)
class EfsVolumeConfiguration(AbstractTerraformBlock):
    file_system_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="efs_volume_configuration")
    authorization_config: Optional[Sequence[AuthorizationConfig]] = None
    root_directory: Optional[str] = None
    transit_encryption: Optional[str] = None
    transit_encryption_port: Optional[int] = None


@define(kw_only=True, slots=False)
class AuthorizationConfig(AbstractTerraformBlock):
    credentials_parameter: str
    domain: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authorization_config")


@define(kw_only=True, slots=False)
class FsxWindowsFileServerVolumeConfiguration(AbstractTerraformBlock):
    file_system_id: str
    root_directory: str
    _block_type: str = "block"
    _name: str = field(
        alias="_name", default="fsx_windows_file_server_volume_configuration"
    )
    authorization_config: Optional[Sequence[AuthorizationConfig]] = None


@define(kw_only=True, slots=False)
class Volume(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="volume")
    docker_volume_configuration: Optional[Sequence[DockerVolumeConfiguration]] = None
    efs_volume_configuration: Optional[Sequence[EfsVolumeConfiguration]] = None
    fsx_windows_file_server_volume_configuration: Optional[
        Sequence[FsxWindowsFileServerVolumeConfiguration]
    ] = None
    host_path: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEcsTaskDefinition(AbstractTerraformResource):
    _group: Any
    _top_name: str
    container_definitions: str
    family: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_task_definition")
    cpu: Optional[str] = None
    ephemeral_storage: Optional[Sequence[EphemeralStorage]] = None
    execution_role_arn: Optional[str] = None
    inference_accelerator: Optional[Sequence[InferenceAccelerator]] = None
    ipc_mode: Optional[str] = None
    memory: Optional[str] = None
    network_mode: Optional[str] = None
    pid_mode: Optional[str] = None
    placement_constraints: Optional[Sequence[PlacementConstraints]] = None
    proxy_configuration: Optional[Sequence[ProxyConfiguration]] = None
    requires_compatibilities: Optional[Sequence[str]] = None
    runtime_platform: Optional[Sequence[RuntimePlatform]] = None
    skip_destroy: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    task_role_arn: Optional[str] = None
    track_latest: Optional[bool] = None
    volume: Optional[Sequence[Volume]] = None
