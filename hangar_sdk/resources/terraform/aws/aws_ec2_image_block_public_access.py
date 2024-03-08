from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2ImageBlockPublicAccess(AbstractTerraformResource):
    _group: Any
    _top_name: str
    state: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_image_block_public_access")
    timeouts: Optional[Timeouts] = None
