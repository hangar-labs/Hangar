from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2Tag(AbstractTerraformResource):
    _group: Any
    _top_name: str
    key: str
    resource_id: str
    value: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_tag")
