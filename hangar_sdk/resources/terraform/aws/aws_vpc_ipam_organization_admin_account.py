from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcIpamOrganizationAdminAccount(AbstractTerraformResource):
    _group: Any
    _top_name: str
    delegated_admin_account_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_ipam_organization_admin_account")
