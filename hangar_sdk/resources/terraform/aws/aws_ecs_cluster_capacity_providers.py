from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DefaultCapacityProviderStrategy(AbstractTerraformBlock):
    capacity_provider: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_capacity_provider_strategy")
    base: Optional[int] = None
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class AwsEcsClusterCapacityProviders(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecs_cluster_capacity_providers")
    capacity_providers: Optional[Sequence[str]] = None
    default_capacity_provider_strategy: Optional[
        Sequence[DefaultCapacityProviderStrategy]
    ] = None
