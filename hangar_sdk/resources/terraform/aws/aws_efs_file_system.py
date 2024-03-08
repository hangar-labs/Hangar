from attr import define,field
from hangar_sdk.resources.terraform import AbstractTerraformBlock,AbstractTerraformResource
from typing import Any,Dict,Optional,Sequence


@define(kw_only=True, slots=False)
class LifecyclePolicy(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="lifecycle_policy")
    transition_to_archive: Optional[str] = None
    transition_to_ia: Optional[str] = None
    transition_to_primary_storage_class: Optional[str] = None


@define(kw_only=True, slots=False)
class Protection(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="protection")
    replication_overwrite: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEfsFileSystem(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_efs_file_system")
    availability_zone_name: Optional[str] = None
    creation_token: Optional[str] = None
    encrypted: Optional[bool] = None
    kms_key_id: Optional[str] = None
    lifecycle_policy: Optional[Sequence[LifecyclePolicy]] = None
    performance_mode: Optional[str] = None
    protection: Optional[Sequence[Protection]] = None
    provisioned_throughput_in_mibps: Optional[int] = None
    tags: Optional[Dict[str,str]] = None
    tags_all: Optional[Dict[str,str]] = None
    throughput_mode: Optional[str] = None


