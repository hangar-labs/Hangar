from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Target(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target")
    port: Optional[int] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsVpclatticeTargetGroupAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    target_group_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpclattice_target_group_attachment")
    target: Optional[Sequence[Target]] = None
    timeouts: Optional[Timeouts] = None
