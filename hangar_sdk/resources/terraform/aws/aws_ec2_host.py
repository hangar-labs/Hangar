from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2Host(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_host")
    asset_id: Optional[str] = None
    auto_placement: Optional[str] = None
    host_recovery: Optional[str] = None
    instance_family: Optional[str] = None
    instance_type: Optional[str] = None
    outpost_arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
