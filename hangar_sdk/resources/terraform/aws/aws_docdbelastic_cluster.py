from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDocdbelasticCluster(AbstractTerraformResource):
    _group: Any
    _top_name: str
    admin_user_name: str
    admin_user_password: str
    auth_type: str
    name: str
    shard_capacity: int
    shard_count: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdbelastic_cluster")
    kms_key_id: Optional[str] = None
    preferred_maintenance_window: Optional[str] = None
    subnet_ids: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
