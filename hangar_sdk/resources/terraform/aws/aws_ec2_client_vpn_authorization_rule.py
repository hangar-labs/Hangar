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
class AwsEc2ClientVpnAuthorizationRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    client_vpn_endpoint_id: str
    target_network_cidr: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_client_vpn_authorization_rule")
    access_group_id: Optional[str] = None
    authorize_all_groups: Optional[bool] = None
    description: Optional[str] = None
    timeouts: Optional[Timeouts] = None
