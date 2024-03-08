from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAmiLaunchPermission(AbstractTerraformResource):
    _group: Any
    _top_name: str
    image_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ami_launch_permission")
    account_id: Optional[str] = None
    organization_arn: Optional[str] = None
    organizational_unit_arn: Optional[str] = None
    terraform_group: Optional[str] = None
