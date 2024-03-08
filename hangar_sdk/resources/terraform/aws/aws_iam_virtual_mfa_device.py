from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamVirtualMfaDevice(AbstractTerraformResource):
    _group: Any
    _top_name: str
    virtual_mfa_device_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_virtual_mfa_device")
    path: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
