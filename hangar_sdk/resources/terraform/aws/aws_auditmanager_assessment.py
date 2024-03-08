from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Roles(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="roles")
    role_arn: Optional[str] = None
    role_type: Optional[str] = None


@define(kw_only=True, slots=False)
class AssessmentReportsDestination(AbstractTerraformBlock):
    destination: str
    destination_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="assessment_reports_destination")


@define(kw_only=True, slots=False)
class AwsAccounts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="aws_accounts")


@define(kw_only=True, slots=False)
class AwsServices(AbstractTerraformBlock):
    service_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="aws_services")


@define(kw_only=True, slots=False)
class Scope(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="scope")
    aws_accounts: Optional[Sequence[AwsAccounts]] = None
    aws_services: Optional[Sequence[AwsServices]] = None


@define(kw_only=True, slots=False)
class AwsAuditmanagerAssessment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    framework_id: str
    name: str
    roles: Sequence[Roles]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_auditmanager_assessment")
    assessment_reports_destination: Optional[Sequence[AssessmentReportsDestination]] = (
        None
    )
    description: Optional[str] = None
    scope: Optional[Sequence[Scope]] = None
    tags: Optional[Dict[str, str]] = None
