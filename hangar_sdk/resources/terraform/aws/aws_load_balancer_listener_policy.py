from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLoadBalancerListenerPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    load_balancer_name: str
    load_balancer_port: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_load_balancer_listener_policy")
    policy_names: Optional[Sequence[str]] = None
    triggers: Optional[Dict[str, str]] = None
