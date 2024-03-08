from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Attribute(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="attribute")


@define(kw_only=True, slots=False)
class AwsLbSslNegotiationPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    lb_port: int
    load_balancer: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lb_ssl_negotiation_policy")
    attribute: Optional[Sequence[Attribute]] = None
    triggers: Optional[Dict[str, str]] = None
