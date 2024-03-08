from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcDhcpOptions(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_dhcp_options")
    domain_name: Optional[str] = None
    domain_name_servers: Optional[Sequence[str]] = None
    netbios_name_servers: Optional[Sequence[str]] = None
    netbios_node_type: Optional[str] = None
    ntp_servers: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
