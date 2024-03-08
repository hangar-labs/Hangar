from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsPinpointApnsSandboxChannel(AbstractTerraformResource):
    _group: Any
    _top_name: str
    application_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_pinpoint_apns_sandbox_channel")
    bundle_id: Optional[str] = None
    certificate: Optional[str] = None
    default_authentication_method: Optional[str] = None
    enabled: Optional[bool] = None
    private_key: Optional[str] = None
    team_id: Optional[str] = None
    token_key: Optional[str] = None
    token_key_id: Optional[str] = None
