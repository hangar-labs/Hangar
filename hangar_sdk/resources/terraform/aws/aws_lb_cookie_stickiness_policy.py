from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLbCookieStickinessPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    lb_port: int
    load_balancer: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lb_cookie_stickiness_policy")
    cookie_expiration_period: Optional[int] = None
