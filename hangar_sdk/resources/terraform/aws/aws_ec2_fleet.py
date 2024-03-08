from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class FleetInstanceSet(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="fleet_instance_set")
    instance_ids: Optional[Sequence[str]] = None
    instance_type: Optional[str] = None
    lifecycle: Optional[str] = None
    platform: Optional[str] = None


@define(kw_only=True, slots=False)
class LaunchTemplateSpecification(AbstractTerraformBlock):
    version: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_specification")
    launch_template_id: Optional[str] = None
    launch_template_name: Optional[str] = None


@define(kw_only=True, slots=False)
class AcceleratorCount(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="accelerator_count")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class AcceleratorTotalMemoryMib(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="accelerator_total_memory_mib")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class BaselineEbsBandwidthMbps(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="baseline_ebs_bandwidth_mbps")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class MemoryGibPerVcpu(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="memory_gib_per_vcpu")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class MemoryMib(AbstractTerraformBlock):
    min: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="memory_mib")
    max: Optional[int] = None


@define(kw_only=True, slots=False)
class NetworkBandwidthGbps(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_bandwidth_gbps")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class NetworkInterfaceCount(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_interface_count")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class TotalLocalStorageGb(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="total_local_storage_gb")
    max: Optional[int] = None
    min: Optional[int] = None


@define(kw_only=True, slots=False)
class VcpuCount(AbstractTerraformBlock):
    min: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vcpu_count")
    max: Optional[int] = None


@define(kw_only=True, slots=False)
class InstanceRequirements(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_requirements")
    accelerator_count: Optional[Sequence[AcceleratorCount]] = None
    accelerator_manufacturers: Optional[Sequence[str]] = None
    accelerator_names: Optional[Sequence[str]] = None
    accelerator_total_memory_mib: Optional[Sequence[AcceleratorTotalMemoryMib]] = None
    accelerator_types: Optional[Sequence[str]] = None
    allowed_instance_types: Optional[Sequence[str]] = None
    bare_metal: Optional[str] = None
    baseline_ebs_bandwidth_mbps: Optional[Sequence[BaselineEbsBandwidthMbps]] = None
    burstable_performance: Optional[str] = None
    cpu_manufacturers: Optional[Sequence[str]] = None
    excluded_instance_types: Optional[Sequence[str]] = None
    instance_generations: Optional[Sequence[str]] = None
    local_storage: Optional[str] = None
    local_storage_types: Optional[Sequence[str]] = None
    memory_gib_per_vcpu: Optional[Sequence[MemoryGibPerVcpu]] = None
    memory_mib: Optional[Sequence[MemoryMib]] = None
    network_bandwidth_gbps: Optional[Sequence[NetworkBandwidthGbps]] = None
    network_interface_count: Optional[Sequence[NetworkInterfaceCount]] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[int] = None
    require_hibernate_support: Optional[bool] = None
    spot_max_price_percentage_over_lowest_price: Optional[int] = None
    total_local_storage_gb: Optional[Sequence[TotalLocalStorageGb]] = None
    vcpu_count: Optional[Sequence[VcpuCount]] = None


@define(kw_only=True, slots=False)
class Override(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="override")
    availability_zone: Optional[str] = None
    instance_requirements: Optional[Sequence[InstanceRequirements]] = None
    instance_type: Optional[str] = None
    max_price: Optional[str] = None
    priority: Optional[int] = None
    subnet_id: Optional[str] = None
    weighted_capacity: Optional[int] = None


@define(kw_only=True, slots=False)
class LaunchTemplateConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_config")
    launch_template_specification: Optional[Sequence[LaunchTemplateSpecification]] = (
        None
    )
    override: Optional[Sequence[Override]] = None


@define(kw_only=True, slots=False)
class OnDemandOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="on_demand_options")
    allocation_strategy: Optional[str] = None
    max_total_price: Optional[str] = None
    min_target_capacity: Optional[int] = None
    single_availability_zone: Optional[bool] = None
    single_instance_type: Optional[bool] = None


@define(kw_only=True, slots=False)
class CapacityRebalance(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_rebalance")
    replacement_strategy: Optional[str] = None
    termination_delay: Optional[int] = None


@define(kw_only=True, slots=False)
class MaintenanceStrategies(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="maintenance_strategies")
    capacity_rebalance: Optional[Sequence[CapacityRebalance]] = None


@define(kw_only=True, slots=False)
class SpotOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="spot_options")
    allocation_strategy: Optional[str] = None
    instance_interruption_behavior: Optional[str] = None
    instance_pools_to_use_count: Optional[int] = None
    maintenance_strategies: Optional[Sequence[MaintenanceStrategies]] = None


@define(kw_only=True, slots=False)
class TargetCapacitySpecification(AbstractTerraformBlock):
    default_target_capacity_type: str
    total_target_capacity: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_capacity_specification")
    on_demand_target_capacity: Optional[int] = None
    spot_target_capacity: Optional[int] = None
    target_capacity_unit_type: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2Fleet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_fleet")
    context: Optional[str] = None
    excess_capacity_termination_policy: Optional[str] = None
    fleet_instance_set: Optional[Sequence[FleetInstanceSet]] = None
    fleet_state: Optional[str] = None
    fulfilled_capacity: Optional[int] = None
    fulfilled_on_demand_capacity: Optional[int] = None
    launch_template_config: Optional[Sequence[LaunchTemplateConfig]] = None
    on_demand_options: Optional[Sequence[OnDemandOptions]] = None
    replace_unhealthy_instances: Optional[bool] = None
    spot_options: Optional[Sequence[SpotOptions]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_capacity_specification: Optional[Sequence[TargetCapacitySpecification]] = (
        None
    )
    terminate_instances: Optional[bool] = None
    terminate_instances_with_expiration: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
    type: Optional[str] = None
    valid_from: Optional[str] = None
    valid_until: Optional[str] = None
