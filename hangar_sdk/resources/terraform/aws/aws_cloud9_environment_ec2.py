from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsCloud9EnvironmentEc2(AbstractTerraformResource):
    _group: Any
    _top_name: str
    image_id: str
    instance_type: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_cloud9_environment_ec2")
    automatic_stop_time_minutes: Optional[int] = None
    connection_type: Optional[str] = None
    description: Optional[str] = None
    owner_arn: Optional[str] = None
    subnet_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
