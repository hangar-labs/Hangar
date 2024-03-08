from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsS3controlAccessPointPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    access_point_arn: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3control_access_point_policy")
