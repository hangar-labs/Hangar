from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class OutputLocation(AbstractTerraformBlock):
    s3_bucket_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="output_location")
    s3_key_prefix: Optional[str] = None
    s3_region: Optional[str] = None


@define(kw_only=True, slots=False)
class Targets(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="targets")


@define(kw_only=True, slots=False)
class AwsSsmAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_association")
    apply_only_at_cron_interval: Optional[bool] = None
    association_name: Optional[str] = None
    automation_target_parameter_name: Optional[str] = None
    compliance_severity: Optional[str] = None
    document_version: Optional[str] = None
    instance_id: Optional[str] = None
    max_concurrency: Optional[str] = None
    max_errors: Optional[str] = None
    output_location: Optional[Sequence[OutputLocation]] = None
    parameters: Optional[Dict[str, str]] = None
    schedule_expression: Optional[str] = None
    sync_compliance: Optional[str] = None
    targets: Optional[Sequence[Targets]] = None
    wait_for_success_timeout_seconds: Optional[int] = None
