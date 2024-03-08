from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2ClientVpnNetworkAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    client_vpn_endpoint_id: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_client_vpn_network_association")
    timeouts: Optional[Timeouts] = None
