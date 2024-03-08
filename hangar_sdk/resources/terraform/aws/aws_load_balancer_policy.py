from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PolicyAttribute(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="policy_attribute")
    name: Optional[str] = None
    value: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLoadBalancerPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    load_balancer_name: str
    policy_name: str
    policy_type_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_load_balancer_policy")
    policy_attribute: Optional[Sequence[PolicyAttribute]] = None
