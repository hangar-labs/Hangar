from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


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
class EbsBlockDevice(AbstractTerraformBlock):
    device_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs_block_device")
    delete_on_termination: Optional[bool] = None
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    snapshot_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class EnclaveOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="enclave_options")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class EphemeralBlockDevice(AbstractTerraformBlock):
    device_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ephemeral_block_device")
    no_device: Optional[bool] = None
    virtual_name: Optional[str] = None


@define(kw_only=True, slots=False)
class SpotOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="spot_options")
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
class LaunchTemplate(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="launch_template")
    name: Optional[str] = None
    version: Optional[str] = None


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
class NetworkInterface(AbstractTerraformBlock):
    device_index: int
    network_interface_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_interface")
    delete_on_termination: Optional[bool] = None
    network_card_index: Optional[int] = None


@define(kw_only=True, slots=False)
class PrivateDnsNameOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="private_dns_name_options")
    enable_resource_name_dns_a_record: Optional[bool] = None
    enable_resource_name_dns_aaaa_record: Optional[bool] = None
    hostname_type: Optional[str] = None


@define(kw_only=True, slots=False)
class RootBlockDevice(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="root_block_device")
    delete_on_termination: Optional[bool] = None
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    read: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_instance")
    ami: Optional[str] = None
    associate_public_ip_address: Optional[bool] = None
    availability_zone: Optional[str] = None
    capacity_reservation_specification: Optional[
        Sequence[CapacityReservationSpecification]
    ] = None
    cpu_core_count: Optional[int] = None
    cpu_options: Optional[Sequence[CpuOptions]] = None
    cpu_threads_per_core: Optional[int] = None
    credit_specification: Optional[Sequence[CreditSpecification]] = None
    disable_api_stop: Optional[bool] = None
    disable_api_termination: Optional[bool] = None
    ebs_block_device: Optional[Sequence[EbsBlockDevice]] = None
    ebs_optimized: Optional[bool] = None
    enclave_options: Optional[Sequence[EnclaveOptions]] = None
    ephemeral_block_device: Optional[Sequence[EphemeralBlockDevice]] = None
    get_password_data: Optional[bool] = None
    hibernation: Optional[bool] = None
    host_id: Optional[str] = None
    host_resource_group_arn: Optional[str] = None
    iam_instance_profile: Optional[str] = None
    instance_initiated_shutdown_behavior: Optional[str] = None
    instance_market_options: Optional[Sequence[InstanceMarketOptions]] = None
    instance_type: Optional[str] = None
    ipv6_address_count: Optional[int] = None
    ipv6_addresses: Optional[Sequence[str]] = None
    key_name: Optional[str] = None
    launch_template: Optional[Sequence[LaunchTemplate]] = None
    maintenance_options: Optional[Sequence[MaintenanceOptions]] = None
    metadata_options: Optional[Sequence[MetadataOptions]] = None
    monitoring: Optional[bool] = None
    network_interface: Optional[Sequence[NetworkInterface]] = None
    placement_group: Optional[str] = None
    placement_partition_number: Optional[int] = None
    private_dns_name_options: Optional[Sequence[PrivateDnsNameOptions]] = None
    private_ip: Optional[str] = None
    root_block_device: Optional[Sequence[RootBlockDevice]] = None
    secondary_private_ips: Optional[Sequence[str]] = None
    security_groups: Optional[Sequence[str]] = None
    source_dest_check: Optional[bool] = None
    subnet_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tenancy: Optional[str] = None
    timeouts: Optional[Timeouts] = None
    user_data: Optional[str] = None
    user_data_base64: Optional[str] = None
    user_data_replace_on_change: Optional[bool] = None
    volume_tags: Optional[Dict[str, str]] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
