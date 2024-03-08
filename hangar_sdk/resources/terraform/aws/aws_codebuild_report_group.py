from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class S3Destination(AbstractTerraformBlock):
    bucket: str
    encryption_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_destination")
    encryption_disabled: Optional[bool] = None
    packaging: Optional[str] = None
    path: Optional[str] = None


@define(kw_only=True, slots=False)
class ExportConfig(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="export_config")
    s3_destination: Optional[Sequence[S3Destination]] = None


@define(kw_only=True, slots=False)
class AwsCodebuildReportGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codebuild_report_group")
    delete_reports: Optional[bool] = None
    export_config: Optional[Sequence[ExportConfig]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
