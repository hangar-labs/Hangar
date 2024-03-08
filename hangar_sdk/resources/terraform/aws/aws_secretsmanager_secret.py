from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Replica(AbstractTerraformBlock):
    region: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replica")
    kms_key_id: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSecretsmanagerSecret(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_secretsmanager_secret")
    description: Optional[str] = None
    force_overwrite_replica_secret: Optional[bool] = None
    kms_key_id: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    policy: Optional[str] = None
    recovery_window_in_days: Optional[int] = None
    replica: Optional[Sequence[Replica]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
