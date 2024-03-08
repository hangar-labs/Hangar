from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayMulticastGroupSource(AbstractTerraformResource):
    _group: Any
    _top_name: str
    group_ip_address: str
    network_interface_id: str
    transit_gateway_multicast_domain_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_multicast_group_source"
    )
