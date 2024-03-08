from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSecurityhubStandardsControl(AbstractTerraformResource):
    _group: Any
    _top_name: str
    control_status: str
    standards_control_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_securityhub_standards_control")
    disabled_reason: Optional[str] = None
