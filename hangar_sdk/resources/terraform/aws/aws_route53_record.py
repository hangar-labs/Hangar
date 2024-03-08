from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Alias(AbstractTerraformBlock):
    evaluate_target_health: bool
    name: str
    zone_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="alias")


@define(kw_only=True, slots=False)
class CidrRoutingPolicy(AbstractTerraformBlock):
    collection_id: str
    location_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cidr_routing_policy")


@define(kw_only=True, slots=False)
class FailoverRoutingPolicy(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="failover_routing_policy")


@define(kw_only=True, slots=False)
class GeolocationRoutingPolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="geolocation_routing_policy")
    continent: Optional[str] = None
    country: Optional[str] = None
    subdivision: Optional[str] = None


@define(kw_only=True, slots=False)
class Coordinates(AbstractTerraformBlock):
    latitude: str
    longitude: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="coordinates")


@define(kw_only=True, slots=False)
class GeoproximityRoutingPolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="geoproximity_routing_policy")
    aws_region: Optional[str] = None
    bias: Optional[int] = None
    coordinates: Optional[Sequence[Coordinates]] = None
    local_zone_group: Optional[str] = None


@define(kw_only=True, slots=False)
class LatencyRoutingPolicy(AbstractTerraformBlock):
    region: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="latency_routing_policy")


@define(kw_only=True, slots=False)
class WeightedRoutingPolicy(AbstractTerraformBlock):
    weight: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="weighted_routing_policy")


@define(kw_only=True, slots=False)
class AwsRoute53Record(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    type: str
    zone_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_record")
    alias: Optional[Sequence[Alias]] = None
    allow_overwrite: Optional[bool] = None
    cidr_routing_policy: Optional[Sequence[CidrRoutingPolicy]] = None
    failover_routing_policy: Optional[Sequence[FailoverRoutingPolicy]] = None
    geolocation_routing_policy: Optional[Sequence[GeolocationRoutingPolicy]] = None
    geoproximity_routing_policy: Optional[Sequence[GeoproximityRoutingPolicy]] = None
    health_check_id: Optional[str] = None
    latency_routing_policy: Optional[Sequence[LatencyRoutingPolicy]] = None
    multivalue_answer_routing_policy: Optional[bool] = None
    records: Optional[Sequence[str]] = None
    set_identifier: Optional[str] = None
    ttl: Optional[int] = None
    weighted_routing_policy: Optional[Sequence[WeightedRoutingPolicy]] = None
