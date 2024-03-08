from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PortInfo(AbstractTerraformBlock):
    from_port: int
    protocol: str
    to_port: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="port_info")
    cidr_list_aliases: Optional[Sequence[str]] = None
    cidrs: Optional[Sequence[str]] = None
    ipv6_cidrs: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class AwsLightsailInstancePublicPorts(AbstractTerraformResource):
    _group: Any
    _top_name: str
    instance_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_instance_public_ports")
    port_info: Optional[Sequence[PortInfo]] = None
