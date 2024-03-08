from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbInstanceAutomatedBackupsReplication(AbstractTerraformResource):
    _group: Any
    _top_name: str
    source_db_instance_arn: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_db_instance_automated_backups_replication"
    )
    kms_key_id: Optional[str] = None
    pre_signed_url: Optional[str] = None
    retention_period: Optional[int] = None
    timeouts: Optional[Timeouts] = None
