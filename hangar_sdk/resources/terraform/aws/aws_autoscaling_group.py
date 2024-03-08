from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class InitialLifecycleHook(AbstractTerraformBlock):
    lifecycle_transition: str
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="initial_lifecycle_hook")
    default_result: Optional[str] = None
    heartbeat_timeout: Optional[int] = None
    notification_metadata: Optional[str] = None
    notification_target_arn: Optional[str] = None
    role_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class InstanceMaintenancePolicy(AbstractTerraformBlock):
    max_healthy_percentage: int
    min_healthy_percentage: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_maintenance_policy")


@define(kw_only=True, slots=False)
class Preferences(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="preferences")
    auto_rollback: Optional[bool] = None
    checkpoint_delay: Optional[str] = None
    checkpoint_percentages: Optional[Sequence[int]] = None
    instance_warmup: Optional[str] = None
    max_healthy_percentage: Optional[int] = None
    min_healthy_percentage: Optional[int] = None
    scale_in_protected_instances: Optional[str] = None
    skip_matching: Optional[bool] = None
    standby_instances: Optional[str] = None


@define(kw_only=True, slots=False)
class InstanceRefresh(AbstractTerraformBlock):
    strategy: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_refresh")
    preferences: Optional[Sequence[Preferences]] = None
    triggers: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class InstancesDistribution(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instances_distribution")
    on_demand_allocation_strategy: Optional[str] = None
    on_demand_base_capacity: Optional[int] = None
    on_demand_percentage_above_base_capacity: Optional[int] = None
    spot_allocation_strategy: Optional[str] = None
    spot_instance_pools: Optional[int] = None
    spot_max_price: Optional[str] = None


@define(kw_only=True, slots=False)
class LaunchTemplateSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_specification")
    launch_template_id: Optional[str] = None
    launch_template_name: Optional[str] = None
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
class LaunchTemplateSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template_specification")
    launch_template_id: Optional[str] = None
    launch_template_name: Optional[str] = None
    version: Optional[str] = None


@define(kw_only=True, slots=False)
class Override(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="override")
    instance_requirements: Optional[Sequence[InstanceRequirements]] = None
    instance_type: Optional[str] = None
    launch_template_specification: Optional[Sequence[LaunchTemplateSpecification]] = (
        None
    )
    weighted_capacity: Optional[str] = None


@define(kw_only=True, slots=False)
class LaunchTemplate(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template")
    launch_template_specification: Optional[Sequence[LaunchTemplateSpecification]] = (
        None
    )
    override: Optional[Sequence[Override]] = None


@define(kw_only=True, slots=False)
class LaunchTemplate(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template")
    name: Optional[str] = None
    version: Optional[str] = None


@define(kw_only=True, slots=False)
class MixedInstancesPolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="mixed_instances_policy")
    instances_distribution: Optional[Sequence[InstancesDistribution]] = None
    launch_template: Optional[Sequence[LaunchTemplate]] = None


@define(kw_only=True, slots=False)
class Tag(AbstractTerraformBlock):
    key: str
    propagate_at_launch: bool
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class TrafficSource(AbstractTerraformBlock):
    identifier: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="traffic_source")
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class InstanceReusePolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_reuse_policy")
    reuse_on_scale_in: Optional[bool] = None


@define(kw_only=True, slots=False)
class WarmPool(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="warm_pool")
    instance_reuse_policy: Optional[Sequence[InstanceReusePolicy]] = None
    max_group_prepared_capacity: Optional[int] = None
    min_size: Optional[int] = None
    pool_state: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsAutoscalingGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    max_size: int
    min_size: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_autoscaling_group")
    availability_zones: Optional[Sequence[str]] = None
    capacity_rebalance: Optional[bool] = None
    context: Optional[str] = None
    default_cooldown: Optional[int] = None
    default_instance_warmup: Optional[int] = None
    desired_capacity: Optional[int] = None
    desired_capacity_type: Optional[str] = None
    enabled_metrics: Optional[Sequence[str]] = None
    force_delete: Optional[bool] = None
    force_delete_warm_pool: Optional[bool] = None
    health_check_grace_period: Optional[int] = None
    health_check_type: Optional[str] = None
    ignore_failed_scaling_activities: Optional[bool] = None
    initial_lifecycle_hook: Optional[Sequence[InitialLifecycleHook]] = None
    instance_maintenance_policy: Optional[Sequence[InstanceMaintenancePolicy]] = None
    instance_refresh: Optional[Sequence[InstanceRefresh]] = None
    launch_configuration: Optional[str] = None
    launch_template: Optional[Sequence[LaunchTemplate]] = None
    load_balancers: Optional[Sequence[str]] = None
    max_instance_lifetime: Optional[int] = None
    metrics_granularity: Optional[str] = None
    min_elb_capacity: Optional[int] = None
    mixed_instances_policy: Optional[Sequence[MixedInstancesPolicy]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    placement_group: Optional[str] = None
    protect_from_scale_in: Optional[bool] = None
    service_linked_role_arn: Optional[str] = None
    suspended_processes: Optional[Sequence[str]] = None
    tag: Optional[Sequence[Tag]] = None
    target_group_arns: Optional[Sequence[str]] = None
    termination_policies: Optional[Sequence[str]] = None
    timeouts: Optional[Timeouts] = None
    traffic_source: Optional[Sequence[TrafficSource]] = None
    vpc_zone_identifier: Optional[Sequence[str]] = None
    wait_for_capacity_timeout: Optional[str] = None
    wait_for_elb_capacity: Optional[int] = None
    warm_pool: Optional[Sequence[WarmPool]] = None
