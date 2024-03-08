from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLoadBalancerBackendServerPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    instance_port: int
    load_balancer_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_load_balancer_backend_server_policy")
    policy_names: Optional[Sequence[str]] = None
