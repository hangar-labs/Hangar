from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EncryptionConfiguration(AbstractTerraformBlock):
    kms_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="encryption_configuration")


@define(kw_only=True, slots=False)
class HealthCheckConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="health_check_configuration")
    healthy_threshold: Optional[int] = None
    interval: Optional[int] = None
    path: Optional[str] = None
    protocol: Optional[str] = None
    timeout: Optional[int] = None
    unhealthy_threshold: Optional[int] = None


@define(kw_only=True, slots=False)
class InstanceConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="instance_configuration")
    cpu: Optional[str] = None
    instance_role_arn: Optional[str] = None
    memory: Optional[str] = None


@define(kw_only=True, slots=False)
class EgressConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="egress_configuration")
    egress_type: Optional[str] = None
    vpc_connector_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class IngressConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ingress_configuration")
    is_publicly_accessible: Optional[bool] = None


@define(kw_only=True, slots=False)
class NetworkConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="network_configuration")
    egress_configuration: Optional[Sequence[EgressConfiguration]] = None
    ingress_configuration: Optional[Sequence[IngressConfiguration]] = None
    ip_address_type: Optional[str] = None


@define(kw_only=True, slots=False)
class ObservabilityConfiguration(AbstractTerraformBlock):
    observability_enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="observability_configuration")
    observability_configuration_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class AuthenticationConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authentication_configuration")
    access_role_arn: Optional[str] = None
    connection_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class CodeConfigurationValues(AbstractTerraformBlock):
    runtime: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="code_configuration_values")
    build_command: Optional[str] = None
    port: Optional[str] = None
    runtime_environment_secrets: Optional[Dict[str, str]] = None
    runtime_environment_variables: Optional[Dict[str, str]] = None
    start_command: Optional[str] = None


@define(kw_only=True, slots=False)
class CodeConfiguration(AbstractTerraformBlock):
    configuration_source: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="code_configuration")
    code_configuration_values: Optional[Sequence[CodeConfigurationValues]] = None


@define(kw_only=True, slots=False)
class SourceCodeVersion(AbstractTerraformBlock):
    type: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_code_version")


@define(kw_only=True, slots=False)
class CodeRepository(AbstractTerraformBlock):
    repository_url: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="code_repository")
    code_configuration: Optional[Sequence[CodeConfiguration]] = None
    source_code_version: Optional[Sequence[SourceCodeVersion]] = None
    source_directory: Optional[str] = None


@define(kw_only=True, slots=False)
class ImageConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="image_configuration")
    port: Optional[str] = None
    runtime_environment_secrets: Optional[Dict[str, str]] = None
    runtime_environment_variables: Optional[Dict[str, str]] = None
    start_command: Optional[str] = None


@define(kw_only=True, slots=False)
class ImageRepository(AbstractTerraformBlock):
    image_identifier: str
    image_repository_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="image_repository")
    image_configuration: Optional[Sequence[ImageConfiguration]] = None


@define(kw_only=True, slots=False)
class SourceConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_configuration")
    authentication_configuration: Optional[Sequence[AuthenticationConfiguration]] = None
    auto_deployments_enabled: Optional[bool] = None
    code_repository: Optional[Sequence[CodeRepository]] = None
    image_repository: Optional[Sequence[ImageRepository]] = None


@define(kw_only=True, slots=False)
class AwsApprunnerService(AbstractTerraformResource):
    _group: Any
    _top_name: str
    service_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apprunner_service")
    auto_scaling_configuration_arn: Optional[str] = None
    encryption_configuration: Optional[Sequence[EncryptionConfiguration]] = None
    health_check_configuration: Optional[Sequence[HealthCheckConfiguration]] = None
    instance_configuration: Optional[Sequence[InstanceConfiguration]] = None
    network_configuration: Optional[Sequence[NetworkConfiguration]] = None
    observability_configuration: Optional[Sequence[ObservabilityConfiguration]] = None
    source_configuration: Optional[Sequence[SourceConfiguration]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
