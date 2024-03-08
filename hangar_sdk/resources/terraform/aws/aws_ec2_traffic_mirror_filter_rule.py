from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DestinationPortRange(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination_port_range")
    from_port: Optional[int] = None
    to_port: Optional[int] = None


@define(kw_only=True, slots=False)
class SourcePortRange(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_port_range")
    from_port: Optional[int] = None
    to_port: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsEc2TrafficMirrorFilterRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination_cidr_block: str
    rule_action: str
    rule_number: int
    source_cidr_block: str
    traffic_direction: str
    traffic_mirror_filter_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_traffic_mirror_filter_rule")
    description: Optional[str] = None
    destination_port_range: Optional[Sequence[DestinationPortRange]] = None
    protocol: Optional[int] = None
    source_port_range: Optional[Sequence[SourcePortRange]] = None
