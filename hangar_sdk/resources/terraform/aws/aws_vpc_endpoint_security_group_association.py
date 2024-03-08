from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcEndpointSecurityGroupAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    security_group_id: str
    vpc_endpoint_id: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_vpc_endpoint_security_group_association"
    )
    replace_default_association: Optional[bool] = None
