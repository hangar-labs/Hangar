from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Details(AbstractTerraformBlock):
    name: str
    policy: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="details")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3controlMultiRegionAccessPointPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3control_multi_region_access_point_policy"
    )
    account_id: Optional[str] = None
    details: Optional[Sequence[Details]] = None
    timeouts: Optional[Timeouts] = None
