from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ManagedScaling(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="managed_scaling")
    instance_warmup_period: Optional[int] = None
    maximum_scaling_step_size: Optional[int] = None
    minimum_scaling_step_size: Optional[int] = None
    status: Optional[str] = None
    target_capacity: Optional[int] = None


@define(kw_only=True, slots=False)
class AutoScalingGroupProvider(AbstractTerraformBlock):
    auto_scaling_group_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="auto_scaling_group_provider")
    managed_draining: Optional[str] = None
    managed_scaling: Optional[Sequence[ManagedScaling]] = None
    managed_termination_protection: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEcsCapacityProvider(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_capacity_provider")
    auto_scaling_group_provider: Optional[Sequence[AutoScalingGroupProvider]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
