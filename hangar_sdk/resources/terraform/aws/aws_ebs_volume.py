from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEbsVolume(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ebs_volume")
    encrypted: Optional[bool] = None
    final_snapshot: Optional[bool] = None
    iops: Optional[int] = None
    kms_key_id: Optional[str] = None
    multi_attach_enabled: Optional[bool] = None
    outpost_arn: Optional[str] = None
    size: Optional[int] = None
    snapshot_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    throughput: Optional[int] = None
    timeouts: Optional[Timeouts] = None
    type: Optional[str] = None
