from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2TransitGatewayPolicyTableAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    transit_gateway_attachment_id: str
    transit_gateway_policy_table_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_ec2_transit_gateway_policy_table_association"
    )
