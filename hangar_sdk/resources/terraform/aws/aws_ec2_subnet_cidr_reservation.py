from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2SubnetCidrReservation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cidr_block: str
    reservation_type: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_subnet_cidr_reservation")
    description: Optional[str] = None
