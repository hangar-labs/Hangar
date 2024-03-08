from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class MinimumHealthyHosts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="minimum_healthy_hosts")
    type: Optional[str] = None
    value: Optional[int] = None


@define(kw_only=True, slots=False)
class TimeBasedCanary(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="time_based_canary")
    interval: Optional[int] = None
    percentage: Optional[int] = None


@define(kw_only=True, slots=False)
class TimeBasedLinear(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="time_based_linear")
    interval: Optional[int] = None
    percentage: Optional[int] = None


@define(kw_only=True, slots=False)
class TrafficRoutingConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="traffic_routing_config")
    time_based_canary: Optional[Sequence[TimeBasedCanary]] = None
    time_based_linear: Optional[Sequence[TimeBasedLinear]] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsCodedeployDeploymentConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    deployment_config_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codedeploy_deployment_config")
    compute_platform: Optional[str] = None
    minimum_healthy_hosts: Optional[Sequence[MinimumHealthyHosts]] = None
    traffic_routing_config: Optional[Sequence[TrafficRoutingConfig]] = None
