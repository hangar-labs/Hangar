from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class CapacityProviderStrategy(AbstractTerraformBlock):
    capacity_provider: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_provider_strategy")
    base: Optional[int] = None
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class NetworkConfiguration(AbstractTerraformBlock):
    subnets: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_configuration")
    assign_public_ip: Optional[bool] = None
    security_groups: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Environment(AbstractTerraformBlock):
    key: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="environment")


@define(kw_only=True, slots=False)
class ResourceRequirements(AbstractTerraformBlock):
    type: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="resource_requirements")


@define(kw_only=True, slots=False)
class ContainerOverrides(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="container_overrides")
    command: Optional[Sequence[str]] = None
    cpu: Optional[int] = None
    environment: Optional[Sequence[Environment]] = None
    memory: Optional[int] = None
    memory_reservation: Optional[int] = None
    resource_requirements: Optional[Sequence[ResourceRequirements]] = None


@define(kw_only=True, slots=False)
class InferenceAcceleratorOverrides(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="inference_accelerator_overrides")
    device_name: Optional[str] = None
    device_type: Optional[str] = None


@define(kw_only=True, slots=False)
class Overrides(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="overrides")
    container_overrides: Optional[Sequence[ContainerOverrides]] = None
    cpu: Optional[str] = None
    execution_role_arn: Optional[str] = None
    inference_accelerator_overrides: Optional[
        Sequence[InferenceAcceleratorOverrides]
    ] = None
    memory: Optional[str] = None
    task_role_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class PlacementConstraints(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="placement_constraints")
    expression: Optional[str] = None


@define(kw_only=True, slots=False)
class PlacementStrategy(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="placement_strategy")
    field: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsEcsTaskExecution(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    cluster: str
    task_definition: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ecs_task_execution")
    capacity_provider_strategy: Optional[Sequence[CapacityProviderStrategy]] = None
    client_token: Optional[str] = None
    desired_count: Optional[int] = None
    enable_ecs_managed_tags: Optional[bool] = None
    enable_execute_command: Optional[bool] = None
    launch_type: Optional[str] = None
    network_configuration: Optional[Sequence[NetworkConfiguration]] = None
    overrides: Optional[Sequence[Overrides]] = None
    placement_constraints: Optional[Sequence[PlacementConstraints]] = None
    placement_strategy: Optional[Sequence[PlacementStrategy]] = None
    platform_version: Optional[str] = None
    propagate_tags: Optional[str] = None
    reference_id: Optional[str] = None
    started_by: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    terraform_group: Optional[str] = None
