from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Alarms(AbstractTerraformBlock):
    alarm_names: Sequence[str]
    enable: bool
    rollback: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="alarms")


@define(kw_only=True, slots=False)
class CapacityProviderStrategy(AbstractTerraformBlock):
    capacity_provider: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="capacity_provider_strategy")
    base: Optional[int] = None
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class DeploymentCircuitBreaker(AbstractTerraformBlock):
    enable: bool
    rollback: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="deployment_circuit_breaker")


@define(kw_only=True, slots=False)
class DeploymentController(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="deployment_controller")
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class LoadBalancer(AbstractTerraformBlock):
    container_name: str
    container_port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="load_balancer")
    elb_name: Optional[str] = None
    target_group_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class NetworkConfiguration(AbstractTerraformBlock):
    subnets: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_configuration")
    assign_public_ip: Optional[bool] = None
    security_groups: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class OrderedPlacementStrategy(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ordered_placement_strategy")
    field: Optional[str] = None


@define(kw_only=True, slots=False)
class PlacementConstraints(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="placement_constraints")
    expression: Optional[str] = None


@define(kw_only=True, slots=False)
class SecretOption(AbstractTerraformBlock):
    name: str
    value_from: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secret_option")


@define(kw_only=True, slots=False)
class LogConfiguration(AbstractTerraformBlock):
    log_driver: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="log_configuration")
    options: Optional[Dict[str, str]] = None
    secret_option: Optional[Sequence[SecretOption]] = None


@define(kw_only=True, slots=False)
class ClientAlias(AbstractTerraformBlock):
    port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="client_alias")
    dns_name: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeout(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeout")
    idle_timeout_seconds: Optional[int] = None
    per_request_timeout_seconds: Optional[int] = None


@define(kw_only=True, slots=False)
class IssuerCertAuthority(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="issuer_cert_authority")
    aws_pca_authority_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Tls(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tls")
    issuer_cert_authority: Optional[Sequence[IssuerCertAuthority]] = None
    kms_key: Optional[str] = None
    role_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Service(AbstractTerraformBlock):
    port_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="service")
    client_alias: Optional[Sequence[ClientAlias]] = None
    discovery_name: Optional[str] = None
    ingress_port_override: Optional[int] = None
    timeout: Optional[Sequence[Timeout]] = None
    tls: Optional[Sequence[Tls]] = None


@define(kw_only=True, slots=False)
class ServiceConnectConfiguration(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="service_connect_configuration")
    log_configuration: Optional[Sequence[LogConfiguration]] = None
    namespace: Optional[str] = None
    service: Optional[Sequence[Service]] = None


@define(kw_only=True, slots=False)
class ServiceRegistries(AbstractTerraformBlock):
    registry_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="service_registries")
    container_name: Optional[str] = None
    container_port: Optional[int] = None
    port: Optional[int] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEcsService(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_service")
    alarms: Optional[Sequence[Alarms]] = None
    capacity_provider_strategy: Optional[Sequence[CapacityProviderStrategy]] = None
    cluster: Optional[str] = None
    deployment_circuit_breaker: Optional[Sequence[DeploymentCircuitBreaker]] = None
    deployment_controller: Optional[Sequence[DeploymentController]] = None
    deployment_maximum_percent: Optional[int] = None
    deployment_minimum_healthy_percent: Optional[int] = None
    desired_count: Optional[int] = None
    enable_ecs_managed_tags: Optional[bool] = None
    enable_execute_command: Optional[bool] = None
    force_new_deployment: Optional[bool] = None
    health_check_grace_period_seconds: Optional[int] = None
    iam_role: Optional[str] = None
    launch_type: Optional[str] = None
    load_balancer: Optional[Sequence[LoadBalancer]] = None
    network_configuration: Optional[Sequence[NetworkConfiguration]] = None
    ordered_placement_strategy: Optional[Sequence[OrderedPlacementStrategy]] = None
    placement_constraints: Optional[Sequence[PlacementConstraints]] = None
    platform_version: Optional[str] = None
    propagate_tags: Optional[str] = None
    scheduling_strategy: Optional[str] = None
    service_connect_configuration: Optional[Sequence[ServiceConnectConfiguration]] = (
        None
    )
    service_registries: Optional[Sequence[ServiceRegistries]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    task_definition: Optional[str] = None
    timeouts: Optional[Timeouts] = None
    triggers: Optional[Dict[str, str]] = None
    wait_for_steady_state: Optional[bool] = None
