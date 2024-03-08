from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Endpoint(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="endpoint")
    region: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class GeoProximityLocation(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="geo_proximity_location")
    bias: Optional[str] = None
    endpoint_reference: Optional[str] = None
    evaluate_target_health: Optional[bool] = None
    health_check: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    region: Optional[str] = None
    rule_reference: Optional[str] = None


@define(kw_only=True, slots=False)
class Items(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="items")
    endpoint_reference: Optional[str] = None
    health_check: Optional[str] = None


@define(kw_only=True, slots=False)
class Location(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="location")
    continent: Optional[str] = None
    country: Optional[str] = None
    endpoint_reference: Optional[str] = None
    evaluate_target_health: Optional[bool] = None
    health_check: Optional[str] = None
    is_default: Optional[bool] = None
    rule_reference: Optional[str] = None
    subdivision: Optional[str] = None


@define(kw_only=True, slots=False)
class Primary(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="primary")
    endpoint_reference: Optional[str] = None
    evaluate_target_health: Optional[bool] = None
    health_check: Optional[str] = None
    rule_reference: Optional[str] = None


@define(kw_only=True, slots=False)
class Region(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="region")
    endpoint_reference: Optional[str] = None
    evaluate_target_health: Optional[bool] = None
    health_check: Optional[str] = None
    region: Optional[str] = None
    rule_reference: Optional[str] = None


@define(kw_only=True, slots=False)
class Secondary(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secondary")
    endpoint_reference: Optional[str] = None
    evaluate_target_health: Optional[bool] = None
    health_check: Optional[str] = None
    rule_reference: Optional[str] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    geo_proximity_location: Optional[Sequence[GeoProximityLocation]] = None
    items: Optional[Sequence[Items]] = None
    location: Optional[Sequence[Location]] = None
    primary: Optional[Sequence[Primary]] = None
    region: Optional[Sequence[Region]] = None
    secondary: Optional[Sequence[Secondary]] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsRoute53TrafficPolicyDocument(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_route53_traffic_policy_document")
    endpoint: Optional[Sequence[Endpoint]] = None
    record_type: Optional[str] = None
    rule: Optional[Sequence[Rule]] = None
    start_endpoint: Optional[str] = None
    start_rule: Optional[str] = None
    version: Optional[str] = None
