from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAuditmanagerAssessmentDelegation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    assessment_id: str
    control_set_id: str
    role_arn: str
    role_type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_auditmanager_assessment_delegation")
    comment: Optional[str] = None
