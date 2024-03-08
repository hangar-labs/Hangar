from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RepositoryFilter(AbstractTerraformBlock):
    filter: str
    filter_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="repository_filter")


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    scan_frequency: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    repository_filter: Optional[Sequence[RepositoryFilter]] = None


@define(kw_only=True, slots=False)
class AwsEcrRegistryScanningConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    scan_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecr_registry_scanning_configuration")
    rule: Optional[Sequence[Rule]] = None
