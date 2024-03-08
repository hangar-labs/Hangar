from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Route(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="route")
    cidr_block: Optional[str] = None
    destination_prefix_list_id: Optional[str] = None
    instance_id: Optional[str] = None
    network_interface_id: Optional[str] = None
    core_network_arn: Optional[str] = None
    egress_only_gateway_id: Optional[str] = None
    ipv6_cidr_block: Optional[str] = None
    nat_gateway_id: Optional[str] = None
    gateway_id: Optional[str] = None
    transit_gateway_id: Optional[str] = None
    vpc_endpoint_id: Optional[str] = None
    vpc_peering_connection_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDefaultRouteTable(AbstractTerraformResource):
    _group: Any
    _top_name: str
    default_route_table_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_default_route_table")
    propagating_vgws: Optional[Sequence[str]] = None
    route: Optional[Sequence[Route]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
