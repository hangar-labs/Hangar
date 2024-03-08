from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLightsailStaticIpAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    instance_name: str
    static_ip_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_static_ip_attachment")
