from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EbsBlockDevice(AbstractTerraformBlock):
    device_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs_block_device")
    delete_on_termination: Optional[bool] = None
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    snapshot_id: Optional[str] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class EphemeralBlockDevice(AbstractTerraformBlock):
    device_name: str
    virtual_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ephemeral_block_device")


@define(kw_only=True, slots=False)
class RootBlockDevice(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="root_block_device")
    delete_on_termination: Optional[bool] = None
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class LaunchSpecification(AbstractTerraformBlock):
    ami: str
    instance_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_specification")
    associate_public_ip_address: Optional[bool] = None
    availability_zone: Optional[str] = None
    ebs_block_device: Optional[Sequence[EbsBlockDevice]] = None
    ebs_optimized: Optional[bool] = None
    ephemeral_block_device: Optional[Sequence[EphemeralBlockDevice]] = None
    iam_instance_profile: Optional[str] = None
    iam_instance_profile_arn: Optional[str] = None
    key_name: Optional[str] = None
    monitoring: Optional[bool] = None
    placement_group: Optional[str] = None
    placement_tenancy: Optional[str] = None
    root_block_device: Optional[Sequence[RootBlockDevice]] = None
    spot_price: Optional[str] = None
    subnet_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    user_data: Optional[str] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
    weighted_capacity: Optional[str] = None


@define(kw_only=True, slots=False)
class LaunchTemplateSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_specification")
    name: Optional[str] = None
    version: Optional[str] = None


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
    _block_type: str = "block"
    _name: str = field(alias="_name", default="memory_mib")
    max: Optional[int] = None
    min: Optional[int] = None


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
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vcpu_count")
    max: Optional[int] = None
    min: Optional[int] = None


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
class Overrides(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="overrides")
    availability_zone: Optional[str] = None
    instance_requirements: Optional[Sequence[InstanceRequirements]] = None
    instance_type: Optional[str] = None
    priority: Optional[int] = None
    spot_price: Optional[str] = None
    subnet_id: Optional[str] = None
    weighted_capacity: Optional[int] = None


@define(kw_only=True, slots=False)
class LaunchTemplateConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_config")
    launch_template_specification: Optional[Sequence[LaunchTemplateSpecification]] = (
        None
    )
    overrides: Optional[Sequence[Overrides]] = None


@define(kw_only=True, slots=False)
class CapacityRebalance(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_rebalance")
    replacement_strategy: Optional[str] = None


@define(kw_only=True, slots=False)
class SpotMaintenanceStrategies(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="spot_maintenance_strategies")
    capacity_rebalance: Optional[Sequence[CapacityRebalance]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSpotFleetRequest(AbstractTerraformResource):
    _group: Any
    _top_name: str
    iam_fleet_role: str
    target_capacity: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_spot_fleet_request")
    allocation_strategy: Optional[str] = None
    context: Optional[str] = None
    excess_capacity_termination_policy: Optional[str] = None
    fleet_type: Optional[str] = None
    instance_interruption_behaviour: Optional[str] = None
    instance_pools_to_use_count: Optional[int] = None
    launch_specification: Optional[Sequence[LaunchSpecification]] = None
    launch_template_config: Optional[Sequence[LaunchTemplateConfig]] = None
    load_balancers: Optional[Sequence[str]] = None
    on_demand_allocation_strategy: Optional[str] = None
    on_demand_max_total_price: Optional[str] = None
    on_demand_target_capacity: Optional[int] = None
    replace_unhealthy_instances: Optional[bool] = None
    spot_maintenance_strategies: Optional[Sequence[SpotMaintenanceStrategies]] = None
    spot_price: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_capacity_unit_type: Optional[str] = None
    target_group_arns: Optional[Sequence[str]] = None
    terminate_instances_on_delete: Optional[str] = None
    terminate_instances_with_expiration: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
    valid_from: Optional[str] = None
    valid_until: Optional[str] = None
    wait_for_fulfillment: Optional[bool] = None
