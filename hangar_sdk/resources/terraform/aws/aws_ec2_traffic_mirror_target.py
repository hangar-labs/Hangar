from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TrafficMirrorTarget(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_traffic_mirror_target")
    description: Optional[str] = None
    gateway_load_balancer_endpoint_id: Optional[str] = None
    network_interface_id: Optional[str] = None
    network_load_balancer_arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
