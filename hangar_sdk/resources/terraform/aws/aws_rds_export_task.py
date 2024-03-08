from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRdsExportTask(AbstractTerraformResource):
    _group: Any
    _top_name: str
    export_task_identifier: str
    iam_role_arn: str
    kms_key_id: str
    s3_bucket_name: str
    source_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_export_task")
    export_only: Optional[Sequence[str]] = None
    s3_prefix: Optional[str] = None
    timeouts: Optional[Timeouts] = None
