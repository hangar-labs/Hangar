from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53TrafficPolicyInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    hosted_zone_id: str
    name: str
    traffic_policy_id: str
    traffic_policy_version: int
    ttl: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_traffic_policy_instance")
