from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PublicAccessBlock(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="public_access_block")
    block_public_acls: Optional[bool] = None
    block_public_policy: Optional[bool] = None
    ignore_public_acls: Optional[bool] = None
    restrict_public_buckets: Optional[bool] = None


@define(kw_only=True, slots=False)
class Region(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="region")
    bucket_account_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Details(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="details")
    public_access_block: Optional[Sequence[PublicAccessBlock]] = None
    region: Optional[Sequence[Region]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3controlMultiRegionAccessPoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3control_multi_region_access_point")
    account_id: Optional[str] = None
    details: Optional[Sequence[Details]] = None
    timeouts: Optional[Timeouts] = None
