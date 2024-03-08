from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CapacityProviderStrategy(AbstractTerraformBlock):
    capacity_provider: str
    weight: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_provider_strategy")
    base: Optional[int] = None


@define(kw_only=True, slots=False)
class LoadBalancer(AbstractTerraformBlock):
    container_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="load_balancer")
    container_port: Optional[int] = None
    load_balancer_name: Optional[str] = None
    target_group_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class NetworkConfiguration(AbstractTerraformBlock):
    subnets: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_configuration")
    assign_public_ip: Optional[bool] = None
    security_groups: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Scale(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scale")
    unit: Optional[str] = None
    value: Optional[int] = None


@define(kw_only=True, slots=False)
class ServiceRegistries(AbstractTerraformBlock):
    registry_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="service_registries")
    container_name: Optional[str] = None
    container_port: Optional[int] = None
    port: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsEcsTaskSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster: str
    service: str
    task_definition: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_task_set")
    capacity_provider_strategy: Optional[Sequence[CapacityProviderStrategy]] = None
    external_id: Optional[str] = None
    force_delete: Optional[bool] = None
    launch_type: Optional[str] = None
    load_balancer: Optional[Sequence[LoadBalancer]] = None
    network_configuration: Optional[Sequence[NetworkConfiguration]] = None
    platform_version: Optional[str] = None
    scale: Optional[Sequence[Scale]] = None
    service_registries: Optional[Sequence[ServiceRegistries]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    wait_until_stable: Optional[bool] = None
    wait_until_stable_timeout: Optional[str] = None
