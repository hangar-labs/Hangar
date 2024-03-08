from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpclatticeAccessLogSubscription(AbstractTerraformResource):
    _group: Any
    _top_name: str
    destination_arn: str
    resource_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpclattice_access_log_subscription")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
