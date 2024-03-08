from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    region: str
    registry_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")


@define(kw_only=True, slots=False)
class RepositoryFilter(AbstractTerraformBlock):
    filter: str
    filter_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="repository_filter")


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    destination: Optional[Sequence[Destination]] = None
    repository_filter: Optional[Sequence[RepositoryFilter]] = None


@define(kw_only=True, slots=False)
class ReplicationConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replication_configuration")
    rule: Optional[Sequence[Rule]] = None


@define(kw_only=True, slots=False)
class AwsEcrReplicationConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecr_replication_configuration")
    replication_configuration: Optional[Sequence[ReplicationConfiguration]] = None
