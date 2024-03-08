from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRdsClusterActivityStream(AbstractTerraformResource):
    _group: Any
    _top_name: str
    kms_key_id: str
    mode: str
    resource_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_cluster_activity_stream")
    engine_native_audit_fields_included: Optional[bool] = None
