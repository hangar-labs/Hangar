from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Ebs(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs")
    delete_on_termination: Optional[str] = None
    encrypted: Optional[str] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    snapshot_id: Optional[str] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class BlockDeviceMappings(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="block_device_mappings")
    device_name: Optional[str] = None
    ebs: Optional[Sequence[Ebs]] = None
    no_device: Optional[str] = None
    virtual_name: Optional[str] = None


@define(kw_only=True, slots=False)
class CapacityReservationTarget(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_reservation_target")
    capacity_reservation_id: Optional[str] = None
    capacity_reservation_resource_group_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class CapacityReservationSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_reservation_specification")
    capacity_reservation_preference: Optional[str] = None
    capacity_reservation_target: Optional[Sequence[CapacityReservationTarget]] = None


@define(kw_only=True, slots=False)
class CpuOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cpu_options")
    amd_sev_snp: Optional[str] = None
    core_count: Optional[int] = None
    threads_per_core: Optional[int] = None


@define(kw_only=True, slots=False)
class CreditSpecification(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="credit_specification")
    cpu_credits: Optional[str] = None


@define(kw_only=True, slots=False)
class ElasticGpuSpecifications(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="elastic_gpu_specifications")


@define(kw_only=True, slots=False)
class ElasticInferenceAccelerator(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="elastic_inference_accelerator")


@define(kw_only=True, slots=False)
class EnclaveOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="enclave_options")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class HibernationOptions(AbstractTerraformBlock):
    configured: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="hibernation_options")


@define(kw_only=True, slots=False)
class IamInstanceProfile(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="iam_instance_profile")
    arn: Optional[str] = None
    name: Optional[str] = None


@define(kw_only=True, slots=False)
class SpotOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="spot_options")
    block_duration_minutes: Optional[int] = None
    instance_interruption_behavior: Optional[str] = None
    max_price: Optional[str] = None
    spot_instance_type: Optional[str] = None
    valid_until: Optional[str] = None


@define(kw_only=True, slots=False)
class InstanceMarketOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_market_options")
    market_type: Optional[str] = None
    spot_options: Optional[Sequence[SpotOptions]] = None


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
class LicenseSpecification(AbstractTerraformBlock):
    license_configuration_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="license_specification")


@define(kw_only=True, slots=False)
class MaintenanceOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="maintenance_options")
    auto_recovery: Optional[str] = None


@define(kw_only=True, slots=False)
class MetadataOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metadata_options")
    http_endpoint: Optional[str] = None
    http_protocol_ipv6: Optional[str] = None
    http_put_response_hop_limit: Optional[int] = None
    http_tokens: Optional[str] = None
    instance_metadata_tags: Optional[str] = None


@define(kw_only=True, slots=False)
class Monitoring(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="monitoring")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class NetworkInterfaces(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_interfaces")
    associate_carrier_ip_address: Optional[str] = None
    associate_public_ip_address: Optional[str] = None
    delete_on_termination: Optional[str] = None
    description: Optional[str] = None
    device_index: Optional[int] = None
    interface_type: Optional[str] = None
    ipv4_address_count: Optional[int] = None
    ipv4_addresses: Optional[Sequence[str]] = None
    ipv4_prefix_count: Optional[int] = None
    ipv4_prefixes: Optional[Sequence[str]] = None
    ipv6_address_count: Optional[int] = None
    ipv6_addresses: Optional[Sequence[str]] = None
    ipv6_prefix_count: Optional[int] = None
    ipv6_prefixes: Optional[Sequence[str]] = None
    network_card_index: Optional[int] = None
    network_interface_id: Optional[str] = None
    private_ip_address: Optional[str] = None
    security_groups: Optional[Sequence[str]] = None
    subnet_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Placement(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="placement")
    affinity: Optional[str] = None
    availability_zone: Optional[str] = None
    group_name: Optional[str] = None
    host_id: Optional[str] = None
    host_resource_group_arn: Optional[str] = None
    partition_number: Optional[int] = None
    spread_domain: Optional[str] = None
    tenancy: Optional[str] = None


@define(kw_only=True, slots=False)
class PrivateDnsNameOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="private_dns_name_options")
    enable_resource_name_dns_a_record: Optional[bool] = None
    enable_resource_name_dns_aaaa_record: Optional[bool] = None
    hostname_type: Optional[str] = None


@define(kw_only=True, slots=False)
class TagSpecifications(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag_specifications")
    resource_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class AwsLaunchTemplate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_launch_template")
    block_device_mappings: Optional[Sequence[BlockDeviceMappings]] = None
    capacity_reservation_specification: Optional[
        Sequence[CapacityReservationSpecification]
    ] = None
    cpu_options: Optional[Sequence[CpuOptions]] = None
    credit_specification: Optional[Sequence[CreditSpecification]] = None
    default_version: Optional[int] = None
    description: Optional[str] = None
    disable_api_stop: Optional[bool] = None
    disable_api_termination: Optional[bool] = None
    ebs_optimized: Optional[str] = None
    elastic_gpu_specifications: Optional[Sequence[ElasticGpuSpecifications]] = None
    elastic_inference_accelerator: Optional[Sequence[ElasticInferenceAccelerator]] = (
        None
    )
    enclave_options: Optional[Sequence[EnclaveOptions]] = None
    hibernation_options: Optional[Sequence[HibernationOptions]] = None
    iam_instance_profile: Optional[Sequence[IamInstanceProfile]] = None
    image_id: Optional[str] = None
    instance_initiated_shutdown_behavior: Optional[str] = None
    instance_market_options: Optional[Sequence[InstanceMarketOptions]] = None
    instance_requirements: Optional[Sequence[InstanceRequirements]] = None
    instance_type: Optional[str] = None
    kernel_id: Optional[str] = None
    key_name: Optional[str] = None
    license_specification: Optional[Sequence[LicenseSpecification]] = None
    maintenance_options: Optional[Sequence[MaintenanceOptions]] = None
    metadata_options: Optional[Sequence[MetadataOptions]] = None
    monitoring: Optional[Sequence[Monitoring]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    network_interfaces: Optional[Sequence[NetworkInterfaces]] = None
    placement: Optional[Sequence[Placement]] = None
    private_dns_name_options: Optional[Sequence[PrivateDnsNameOptions]] = None
    ram_disk_id: Optional[str] = None
    security_group_names: Optional[Sequence[str]] = None
    tag_specifications: Optional[Sequence[TagSpecifications]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    update_default_version: Optional[bool] = None
    user_data: Optional[str] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
