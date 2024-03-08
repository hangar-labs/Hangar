from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3controlAccessGrantsInstanceResourcePolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3control_access_grants_instance_resource_policy"
    )
    account_id: Optional[str] = None
