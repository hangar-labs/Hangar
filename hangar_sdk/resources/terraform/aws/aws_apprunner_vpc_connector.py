from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApprunnerVpcConnector(AbstractTerraformResource):
    _group: Any
    _top_name: str
    security_groups: Sequence[str]
    subnets: Sequence[str]
    vpc_connector_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apprunner_vpc_connector")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
