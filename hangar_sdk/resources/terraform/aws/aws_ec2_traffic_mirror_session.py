from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TrafficMirrorSession(AbstractTerraformResource):
    _group: Any
    _top_name: str
    network_interface_id: str
    session_number: int
    traffic_mirror_filter_id: str
    traffic_mirror_target_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_traffic_mirror_session")
    description: Optional[str] = None
    packet_length: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    virtual_network_id: Optional[int] = None
