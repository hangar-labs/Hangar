from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2CapacityReservation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    availability_zone: str
    instance_count: int
    instance_platform: str
    instance_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_capacity_reservation")
    ebs_optimized: Optional[bool] = None
    end_date: Optional[str] = None
    end_date_type: Optional[str] = None
    ephemeral_storage: Optional[bool] = None
    instance_match_criteria: Optional[str] = None
    outpost_arn: Optional[str] = None
    placement_group_arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tenancy: Optional[str] = None
