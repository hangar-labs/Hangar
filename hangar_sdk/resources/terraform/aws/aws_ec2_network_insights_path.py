from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2NetworkInsightsPath(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination: str
    protocol: str
    source: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_network_insights_path")
    destination_ip: Optional[str] = None
    destination_port: Optional[int] = None
    source_ip: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
