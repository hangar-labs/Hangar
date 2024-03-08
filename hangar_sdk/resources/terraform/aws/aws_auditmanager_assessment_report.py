from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAuditmanagerAssessmentReport(AbstractTerraformResource):
    _group: Any
    _top_name: str
    assessment_id: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_auditmanager_assessment_report")
    description: Optional[str] = None
