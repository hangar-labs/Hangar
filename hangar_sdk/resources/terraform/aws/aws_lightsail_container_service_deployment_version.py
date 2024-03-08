from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Container(AbstractTerraformBlock):
    container_name: str
    image: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="container")
    command: Optional[Sequence[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class HealthCheck(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="health_check")
    healthy_threshold: Optional[int] = None
    interval_seconds: Optional[int] = None
    path: Optional[str] = None
    success_codes: Optional[str] = None
    timeout_seconds: Optional[int] = None
    unhealthy_threshold: Optional[int] = None


@define(kw_only=True, slots=False)
class PublicEndpoint(AbstractTerraformBlock):
    container_name: str
    container_port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="public_endpoint")
    health_check: Optional[Sequence[HealthCheck]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLightsailContainerServiceDeploymentVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    service_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_lightsail_container_service_deployment_version"
    )
    container: Optional[Sequence[Container]] = None
    public_endpoint: Optional[Sequence[PublicEndpoint]] = None
    timeouts: Optional[Timeouts] = None
