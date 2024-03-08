from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Optional,Sequence


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")
    availability_zone_name: Optional[str] = None
    file_system_id: Optional[str] = None
    kms_key_id: Optional[str] = None
    region: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEfsReplicationConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    source_file_system_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_replication_configuration")
    destination: Optional[Sequence[Destination]] = None
    timeouts: Optional[Timeouts] = None


